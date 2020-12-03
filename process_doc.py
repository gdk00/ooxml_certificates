from shutil import move
import os
import zipfile
import tempfile
from config import result_path


def updateZip(zipname, result_path, str_to_replace: dict):
    # generate a temp file
    filename = 'word/document.xml'
    tmpfd, tmpname = tempfile.mkstemp(dir=os.path.dirname(zipname))
    os.close(tmpfd)

    # create a temp copy of the archive without filename
    with zipfile.ZipFile(zipname, 'r') as zin:
        with zipfile.ZipFile(tmpname, 'w') as zout:
            zout.comment = zin.comment # preserve the comment
            for item in zin.infolist():
                if item.filename != filename:
                    zout.writestr(item, zin.read(item.filename))
                else:
                    with zin.open(filename) as f:
                        d = f.readlines()
                        new_file = []
                        for i in d:
                            line = ''.join(str(i).split('\'')[1:-1]).replace(r'\r', '').replace(r'\n', '')
                            for k, v in str_to_replace.items():
                                if k in line:
                                    line = line.replace(k, v)
                            new_file.append(line)
                        new_file = ''.join(new_file)
                    zout.writestr(item, new_file)

    # replace with the temp archive
    move(tmpname, result_path)

def create_sertificates(data, template):
    for person in data:
        updateZip(
            zipname=template[person['qualification']],
            result_path=os.path.join(result_path, person['name'] + '.docx'),
            str_to_replace={
                '{name}': person['name'],
                '{date}': person['date'],
                '{place}': person['place']
            }
        )

