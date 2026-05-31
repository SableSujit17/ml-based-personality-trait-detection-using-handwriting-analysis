[Setup]
AppName=Handwriting Personality Analyzer
AppVersion=1.0
DefaultDirName={autopf}\Handwriting Personality Analyzer
DefaultGroupName=Handwriting Personality Analyzer
OutputDir=installer
OutputBaseFilename=HandwritingPersonalityAnalyzer_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=D:\Project\Project 1 -03\Handwriting Analysis App\assets\icon.ico

[Files]
Source: "D:\Project\Project 1 -03\Handwriting Analysis App\FINAL_DESKTOP_APP\Handwriting Personality Analyzer\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Handwriting Personality Analyzer"; Filename: "{app}\Handwriting Personality Analyzer.exe"
Name: "{autodesktop}\Handwriting Personality Analyzer"; Filename: "{app}\Handwriting Personality Analyzer.exe"

[Run]
Filename: "{app}\Handwriting Personality Analyzer.exe"; Description: "Launch Handwriting Personality Analyzer"; Flags: nowait postinstall skipifsilent
