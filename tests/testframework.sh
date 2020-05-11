GREEN="\e[32m"
RED="\e[31m"
RESET_LINE="\r\e[K"
DEFAULT="\e[39m"

function assert {
    trap "echo -e \"$DEFAULT\"" EXIT

    TestName=${FUNCNAME[ 1 ]}
    TestLine=${BASH_LINENO[ 0 ]}

    echo -en $GREEN "Test $TestName:$TestLine \"$@\" : ..."
    #if ! $@; then
    if ! eval $@; then
        echo -e $RESET_LINE $RED "Test $TestName:$TestLine \"$@\" : FAILURE"
    else
        echo -e $RESET_LINE $GREEN "Test $TestName:$TestLine \"$@\" : OK"
    fi


    echo -ne $DEFAULT
}

