# jay
Simple software to back up projects from the command line

### Installation

    mv jay.py jay
    chmod +x jay
    sudo mv jay /bin/jay
    
_Optional; can run without root access by providing path and/or program (e.g. python ~/Programs/jay)_

### Use

    jay
_Display possible arguments_

    jay create
    jay c
_Create a new project in the current directory_

    jay update [optional title]
    jay u [optional title]
_Back up the contents of "./working" to "./optional\ title"_

    jay revert [title]
    jay r [title]
_Replace the contents of "./working" with those of "./title"_

    jay note
    jay n
_Create "./working/note" with text input_
