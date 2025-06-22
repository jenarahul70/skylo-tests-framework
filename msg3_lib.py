# msg3_lib.py  (place it at project root or in a src/ folder)
import re
from pathlib import Path

class Msg3Library:

    def calculate_msg3_success_rate(self, logfile: str) -> float:
        """
        Returns the overall MSG3 success-rate (0-100) found in *logfile*.
        Success line  :  'type MSG3-RRC-C-REQ'  AND  'status success'
        Failure line  :  'type MSG3-UNKNOWN'    AND  'status timeout'
        """
        text = Path(logfile).read_text(encoding="utf-8", errors="ignore")

        success_pat = re.compile(r"type MSG3-RRC-C-REQ.*status success", re.I)
        failure_pat = re.compile(r"type\s+MSG3-UNKNOWN.*status timeout", re.I)

        succ = len(success_pat.findall(text))
        fail = len(failure_pat.findall(text))
        total = succ + fail
        return 0.0 if total == 0 else (succ / total) * 100