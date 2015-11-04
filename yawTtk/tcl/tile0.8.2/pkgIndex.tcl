if {![package vsatisfies [package provide Tcl] 8.4]} { return }
package ifneeded tile 0.8.2 \
    "namespace eval tile { variable library [list $dir] };\
     load \[file join [list $dir] tile082.dll\]"
