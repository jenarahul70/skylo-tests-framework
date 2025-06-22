*** Settings ***
Library    Collections
Library    msg3_lib.Msg3Library    WITH NAME    Msg3

*** Variables ***
${LOG_FILE}         bs_log.txt        # ← variable ① (can be overridden)
${PASS_THRESHOLD}   12                # ← variable ② (can be overridden)

*** Test Cases ***

MSG3 Success-Rate Meets Threshold
    [Documentation]  Pass if success-rate in ${LOG_FILE} ≥ ${PASS_THRESHOLD} %
    ${rate}=    Msg3.Calculate Msg3 Success Rate    ${LOG_FILE}
    Log         Calculated success-rate = ${rate} %
    ${rate}=    Convert To Number      ${rate}
    ${th}=      Convert To Number      ${PASS_THRESHOLD}
    Should Be True    ${rate} >= ${th}
