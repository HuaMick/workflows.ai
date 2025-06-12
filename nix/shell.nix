{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python3.withPackages (ps: with ps; [
    # Testing
    pytest
    pytest-cov
    pytest-mock
    
    # Development tools
    black
    mypy
    ruff
  ]);
in

pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python environment
    pythonEnv
    
    # Development tools
    black
    mypy
    ruff
    
    # Git
    git
  ];

  shellHook = ''
    # Set up Python path
    export PYTHONPATH=$PWD/src:$PYTHONPATH
  '';
} 