let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages = with pkgs; [
    (pkgs.python311.withPackages (
      python-pkgs: with python-pkgs; [
        jupyter
        pip
        praw
        beautifulsoup4
        requests
        numpy
        pandas
        playwright
      ]
    ))
  ];
}
