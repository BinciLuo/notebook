### libclang.dylib
- Error:```dyld: Library not loaded: @rpath/libclang.dylib```
- Solution:```export DYLD_FALLBACK_LIBRARY_PATH="$(xcode-select --print-path)/usr/lib/"```
- [Reference](https://github.com/twistedfall/opencv-rust)