import sys
from pathlib import Path

JPEG_iMAGES = []
PNG_iMAGES = []
JPG_iMAGES = []
SVG_iMAGES= []
AVI_VIDEO = []
MP4_VIDEO = [] 
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = [] 
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_MUSIC = [] 
OGG_MUSIC = [] 
WAV_MUSIC = [] 
AMR_MUSIC = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
MY_OTHER = []

REGISTER_EXTENSION = {
   'JPEG': JPEG_iMAGES ,
   'PNG': PNG_iMAGES, 
   'JPG': JPG_iMAGES, 
   'SVG': SVG_iMAGES,
   'AVI': AVI_VIDEO ,
   'MOV': MOV_VIDEO ,
   'DOC': DOC_DOCUMENTS ,
   'DOCX': DOCX_DOCUMENTS,
   'TXT': TXT_DOCUMENTS, 
   'PDF' : PDF_DOCUMENTS, 
   'XLSX': XLSX_DOCUMENTS ,
   'PPTX': PPTX_DOCUMENTS ,
   'MP3': MP3_MUSIC , 
   'OGG': OGG_MUSIC ,
   'WAV': WAV_MUSIC ,  
   'AMR': AMR_MUSIC ,
   'ZIP': ZIP_ARCHIVES ,
   'GZ': GZ_ARCHIVES ,
   'TAR': TAR_ARCHIVES ,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN= set()

def get_extension(name: str):
    return Path(name).suffix[1:].upper()

def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if iten.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue
        extension = get_extension(item.name)
        full_name = folder / item.name
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)
                MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    print(f'unknow: {UNKNOWN}')
    print(f'my_other: {MY_OTHER}')
    print(f'Images jpeg: {JPEG_iMAGES}')
    print(f'Images png: {PNG_iMAGES}')
    print(f'Images jpg: {JPEG_iMAGES}')
    print(f'Images svg: {SVG_iMAGES}')
    print(f'Video avi: {AVI_VIDEO}')
    print(f'Video mp4: {MP4_VIDEO}')
    print(f'Video mov: {MOV_VIDEO}')
    print(f'Video mkv: {MKV_VIDEO}')
    print(f'Documents doc: {DOC_DOCUMENTS}')
    print(f'Documents docx: {DOCX_DOCUMENTS}')
    print(f'Documents txt: {TXT_DOCUMENTS}')
    print(f'Documents pdf: {PDF_DOCUMENTS}')
    print(f'Documents xlsx: {XLSX_DOCUMENTS}')
    print(f'Documents pptx: {PPTX_DOCUMENTS}')
    print(f'Music mp3: {MP3_MUSIC}')
    print(f'Music ogg: {OGG_MUSIC}')
    print(f'Music wav: {WAV_MUSIC}')
    print(f'Music amr: {AMR_MUSIC}')
    print(f'Archives zip: {ZIP_ARCHIVES}')
    print(f'Archives gz: {GZ_ARCHIVES}')
    print(f'Archives tar: {TAR_ARCHIVES}')
