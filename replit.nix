{ pkgs }: {
  deps = [
    pkgs.espeak-ng
    pkgs.gh
    pkgs.python38Full
    pkgs.espeak
    # pkgs.libespeak-dev
    pkgs.pyttsx3
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}
