let
  pkgs = import <nixpkgs> { };
  # lib = pkgs.lib;
  # gensim = pkgs.python311Packages.buildPythonPackage rec {
  #   pname = "gensim";
  #   version = "4.3.3";
  #   pyproject = true;
  #   build-system = with pkgs.python311Packages; [
  #     setuptools
  #   ];
  #
  #   dependencies = with pkgs.python311Packages; [
  #     numpy
  #     oldest-supported-numpy
  #     cython_0
  #   ];
  #
  #   src = pkgs.fetchPypi {
  #     inherit pname version;
  #     sha256 = "sha256-hIUgdqaj2I19rFviReJMIcO4GbVl4UwbYfo+Xudtz1c=";
  #   };
  #
  #   doCheck = false;
  # };
in
pkgs.mkShell {
  packages = with pkgs; [
    # (pkgs.python311.withPackages (
    #   python-pkgs: with python-pkgs; [
    #     pandas
    #     numpy
    #     sklearn-compat
    #     openai
    #     jupyter
    #   ]
    # ))
    conda
  ];
}
