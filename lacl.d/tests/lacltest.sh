#!/bin/bash

source testframework.sh

TOKEN="lacltest."`date +%s`
FILE_PREFIX="/dev/shm/$TOKEN"

function CheckCleanState {
    for file in "$FILE_PREFIX.{log,ctl,pid}"; do
        if [[ -e $file ]]; then
            >&2 echo "Error: file '$file' exists."
            return `false`
        fi
    done

    if lsof | grep "$TOKEN"; then
        >&2 echo "Error: not all processes were shut down"
        return `false`
    fi

    return `true`
}

function CleanUp {
    # kill all processes that use the current tokens
    for pid in `lsof | grep "$TOKEN" | tr -s ' ' | cut -d ' ' -f 2 | sort -gu`; do
        kill -9 $pid
    done
    # remove all remaining files
    rm -rfv $FILE_PREFIX.{log,pid,ctl} 2>/dev/null
}


#-------------------------------------------------------------------------------------

function SecondTest {
    assert CheckCleanState
    CleanUp
}

function LaclShouldPrintUsageOnInvalidCommands {
    assert CheckCleanState

    assert '[[ `../lacl` = Usage* ]];'
    assert CheckCleanState
    
    assert '[[ `../lacl start` = Usage* ]]'
    assert CheckCleanState

    assert '[[ `../lacl connect` = Usage* ]]'
    assert CheckCleanState

    assert '[[ `../lacl stop` = Usage* ]]'
    assert CheckCleanState

    assert '[[ `../lacl kill` = Usage* ]]'
    assert CheckCleanState

}
#------------------------------------------------------------------------------------

LaclShouldPrintUsageOnInvalidCommands

