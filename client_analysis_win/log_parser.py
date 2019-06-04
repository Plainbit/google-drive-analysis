import re


class SyncLogParser:

    def __init__(self, log_path):
        self._log_path = log_path

    def parse(self, line):

        result = {
            'log_time': '-',
            'file_path': '-',
            'action': '-',
            'request_user': '-',
        }

        log_time = line[0:30].rstrip()

        re_patterns = {
            "filename": r"filename=u'[^']+",
            "reason": "tags=[^,]+",
            "request": r"Write request - [^']+$"
        }

        result['log_time'] = log_time
        for pattern_name, pattern in re_patterns.items():
            re_pattern = re.compile(pattern)
            matches = re_pattern.findall(line)

            for match in matches:
                if pattern_name == 'filename':
                    result['file_path'] = match[11:].encode('utf-8').decode('unicode-escape').replace('\\\\?\\', '')

                elif pattern_name == 'reason':
                    if match.lower().find('create') >= 0:
                        result['action'] = '생성'
                    elif match.lower().find('modify') >= 0:
                        result['action'] = '수정'

                elif pattern_name == 'request':
                    result['request_user'] = match.replace('Write request - ', '').rstrip()

        return result