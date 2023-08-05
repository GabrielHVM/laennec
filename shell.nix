# shell.nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
name = "tcc-shell";
  buildInputs = [
    pkgs.python310Packages.numpy
    pkgs.python310Packages.flask
    pkgs.python310Packages.scipy
    (pkgs.python310Packages.opencv4.override { enableGtk2 = true; })
  ];}
