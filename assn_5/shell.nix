let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages = with pkgs; [
    (pkgs.python312.withPackages (
      pkgs: with pkgs; [
        jupyter
        numpy
        pandas
        matplotlib
        scipy
        scikit-learn
        seaborn
      ]
    ))
  ];
}
