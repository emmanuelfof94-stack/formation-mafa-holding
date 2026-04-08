@echo off
title Gestion Qualite - Serveur HTTPS
color 1F
echo.
echo  ================================================
echo    SYSTEME GESTION QUALITE - DEMARRAGE HTTPS
echo  ================================================
echo.
cd /d "%~dp0"
echo  Demarrage du serveur HTTPS (port 3443)...
echo.
echo  IMPORTANT : Premiere utilisation sur telephone
echo  - Ouvrir le navigateur sur le telephone
echo  - Aller sur l'URL affichee ci-dessous
echo  - Cliquer "Avance" puis "Continuer" pour accepter
echo    le certificat auto-signe (une seule fois)
echo.
start "" "https://localhost:3443/admin"
node server.js
pause
