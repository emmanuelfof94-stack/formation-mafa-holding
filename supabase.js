/**
 * SUPABASE INTEGRATION — Formation MAFA Holding
 * Identifiant unique : numéro de téléphone
 */

const SUPABASE_URL = 'https://jwxwrptjrmnfkdluphee.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp3eHdycHRqcm1uZmtkbHVwaGVlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ1Njc1ODAsImV4cCI6MjA5MDE0MzU4MH0.lDr6x1aPda5jRbRmKi1uLNDd3X__5YlhbNZ5osnHg7s';

let _supabase = null;

function getSupabase() {
  if (!_supabase) {
    _supabase = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
  }
  return _supabase;
}

// ══════════════════════════════════════
// CANDIDATS — identifié par téléphone
// ══════════════════════════════════════

/**
 * Cherche un candidat par téléphone.
 * Retourne l'objet candidat ou null.
 */
async function findCandidatByPhone(telephone) {
  const sb = getSupabase();
  const { data, error } = await sb
    .from('candidats')
    .select('*')
    .eq('telephone', telephone)
    .maybeSingle();

  if (error) {
    console.error('[Supabase] Erreur recherche candidat:', error);
    return null;
  }
  return data;
}

/**
 * Crée ou connecte un candidat par numéro de téléphone.
 * - Si le téléphone existe : retourne le compte existant (connexion)
 * - Sinon : crée un nouveau compte
 */
async function loginOrCreateCandidat({ nom, prenom, telephone, poste }) {
  const sb = getSupabase();

  // Chercher par téléphone
  const existing = await findCandidatByPhone(telephone);

  if (existing) {
    // Compte existant — mettre à jour nom/prenom/poste si changé
    if (existing.nom !== nom || existing.prenom !== prenom || existing.poste !== poste) {
      const { data } = await sb
        .from('candidats')
        .update({ nom, prenom, poste })
        .eq('id', existing.id)
        .select()
        .single();
      return { candidat: data || existing, isNew: false };
    }
    return { candidat: existing, isNew: false };
  }

  // Nouveau compte
  const { data, error } = await sb
    .from('candidats')
    .insert({ nom, prenom, telephone, poste })
    .select()
    .single();

  if (error) {
    console.error('[Supabase] Erreur création candidat:', error);
    return { candidat: null, isNew: false };
  }
  return { candidat: data, isNew: true };
}

// ══════════════════════════════════════
// SCORES (Quiz modules)
// ══════════════════════════════════════

async function saveScore({ candidat_id, module, score, total, details }) {
  const sb = getSupabase();
  const { data, error } = await sb
    .from('scores')
    .insert({ candidat_id, module, score, total, details: details || {} })
    .select()
    .single();

  if (error) {
    console.error('[Supabase] Erreur sauvegarde score:', error);
    return null;
  }
  return data;
}

async function getScores(candidat_id) {
  const sb = getSupabase();
  const { data, error } = await sb
    .from('scores')
    .select('*')
    .eq('candidat_id', candidat_id)
    .order('created_at', { ascending: false });

  if (error) {
    console.error('[Supabase] Erreur lecture scores:', error);
    return [];
  }
  return data || [];
}

// ══════════════════════════════════════
// PROGRESSION
// ══════════════════════════════════════

async function updateProgression({ candidat_id, module, onglet, completed }) {
  const sb = getSupabase();
  const { data, error } = await sb
    .from('progression')
    .upsert(
      { candidat_id, module, onglet, completed, updated_at: new Date().toISOString() },
      { onConflict: 'candidat_id,module,onglet' }
    )
    .select()
    .single();

  if (error) {
    console.error('[Supabase] Erreur progression:', error);
    return null;
  }
  return data;
}

async function getProgression(candidat_id) {
  const sb = getSupabase();
  const { data, error } = await sb
    .from('progression')
    .select('*')
    .eq('candidat_id', candidat_id);

  if (error) {
    console.error('[Supabase] Erreur lecture progression:', error);
    return [];
  }
  return data || [];
}

// ══════════════════════════════════════
// EVALUATIONS
// ══════════════════════════════════════

async function saveEvaluation({ candidat_id, poste, score_final, total_questions, correct, wrong, percentage, reponses, duree_secondes }) {
  const sb = getSupabase();
  const payload = { candidat_id, poste, score_final, total_questions, reponses: reponses || [], duree_secondes };
  if (correct !== undefined) payload.correct = correct;
  if (wrong !== undefined) payload.wrong = wrong;
  if (percentage !== undefined) payload.percentage = percentage;
  const { data, error } = await sb
    .from('evaluations')
    .insert(payload)
    .select()
    .single();

  if (error) {
    console.error('[Supabase] Erreur sauvegarde évaluation:', error);
    return null;
  }
  return data;
}

async function getAllEvaluations() {
  const sb = getSupabase();
  const { data, error } = await sb
    .from('evaluations')
    .select('*, candidats(nom, prenom, telephone, poste)')
    .order('created_at', { ascending: false });

  if (error) {
    console.error('[Supabase] Erreur lecture évaluations:', error);
    return [];
  }
  return data || [];
}

async function getAllResults() {
  const sb = getSupabase();
  const { data, error } = await sb
    .from('evaluations')
    .select('*, candidats(*)')
    .order('created_at', { ascending: false });

  if (error) {
    console.error('[Supabase] Erreur lecture résultats:', error);
    return [];
  }
  return data || [];
}
