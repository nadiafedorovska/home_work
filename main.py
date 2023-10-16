from pathlib import Path
import shutil
import sys
import file_parsel
from normalize import normalize

def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))

def handle_documents(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))

def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ""))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink


def main(folder: Path):
    file_parsel.scan(folder)
    for file in file_parsel.JPEG_iMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in file_parsel.JPG_iMAGES:
        handle_media(file, folder / 'images' / 'JPG')    
    for file in file_parsel.PNG_iMAGES:
        handle_media(file, folder / 'images' / 'PNG')    
    for file in file_parsel.SVG_iMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in file_parsel.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')   
    for file in file_parsel.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')   
    for file in file_parsel.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in file_parsel.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')
    for file in file_parsel.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in file_parsel.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG') 
    for file in file_parsel.WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')   
    for file in file_parsel.AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')   
    for file in file_parsel.DOC_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOC')  
    for file in file_parsel.DOCX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOCX') 
    for file in file_parsel.TXT_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'TXT')  
    for file in file_parsel.PDF_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PDF')       
    for file in file_parsel.XLSX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in file_parsel.PPTX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PPTX')
    for file in file_parsel.DOC_DOCUMENTS:
        handle_media(file, folder / 'MY_OTHER' )
    for file in file_parsel.ZIP_ARCHIVES:
        handle_media(file, folder / 'archives' / 'ZIP')
    for file in file_parsel.GZ_ARCHIVES:
        handle_media(file, folder / 'archives' / 'GZ')
    for file in file_parsel.TAR_ARCHIVES:
        handle_media(file, folder / 'archives' / 'TAR')
    for file in file_parsel.MY_OTHER:
        handle_media(file, folder / 'unknown')

    for folder in file_parsel.FOLDERS[::-1]:
        try :
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')

if __name__ == "__main__":
    folder_process = Path(sys.argv[1])
    main(folder_process.resolve())

