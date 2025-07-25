{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

    packages = [
        (pkgs.python3.withPackages(pypkgs: with pypkgs; [
            numpy
            requests
            pandas
            python-dotenv
            numpy
        ]))
    ];

    shellHook = ''
        echo Entered Python dev environment
    '';
}
