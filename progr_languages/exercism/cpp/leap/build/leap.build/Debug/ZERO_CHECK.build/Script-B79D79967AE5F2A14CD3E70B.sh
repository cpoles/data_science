#!/bin/sh
set -e
if test "$CONFIGURATION" = "Debug"; then :
  cd /Users/krustybr/Programming/data_science/progr_languages/exercism/cpp/leap/build
  make -f /Users/krustybr/Programming/data_science/progr_languages/exercism/cpp/leap/build/CMakeScripts/ReRunCMake.make
fi
if test "$CONFIGURATION" = "Release"; then :
  cd /Users/krustybr/Programming/data_science/progr_languages/exercism/cpp/leap/build
  make -f /Users/krustybr/Programming/data_science/progr_languages/exercism/cpp/leap/build/CMakeScripts/ReRunCMake.make
fi
if test "$CONFIGURATION" = "MinSizeRel"; then :
  cd /Users/krustybr/Programming/data_science/progr_languages/exercism/cpp/leap/build
  make -f /Users/krustybr/Programming/data_science/progr_languages/exercism/cpp/leap/build/CMakeScripts/ReRunCMake.make
fi
if test "$CONFIGURATION" = "RelWithDebInfo"; then :
  cd /Users/krustybr/Programming/data_science/progr_languages/exercism/cpp/leap/build
  make -f /Users/krustybr/Programming/data_science/progr_languages/exercism/cpp/leap/build/CMakeScripts/ReRunCMake.make
fi

