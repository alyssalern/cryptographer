import argparse
import sys
import os
from decryptor import Decryptor

def fix_output_file(output_file, encrypted_file):
    if(output_file is None):
        split_extension = encrypted_file.name.rsplit('.', 1)
        output_file = "{}_decrypted.{}".format(split_extension[0], split_extension[1])

    output_dir = output_file[:output_file.rindex('/')]

    if os.path.isdir(output_dir) is False:
        print("Invalid output file '{}' provided.".format(output_file))
        sys.exit(1)

    return output_file

def getArgs():
    arg_parser = argparse.ArgumentParser(description='File decrypter.')
    arg_parser.add_argument('file', help='Path to the encrypted file to decrypt.', type=argparse.FileType('r'))
    arg_parser.add_argument('--output_file', '-o', help='Path to save the decrypted output file to.', type=str)
    args = arg_parser.parse_args()

    args.output_file = fix_output_file(args.output_file, args.file)
    return args


if __name__ == "__main__":
    #args = getArgs()
    decryptor = Decryptor()
    result = decryptor.decrypt("Znoy oy gt ktixevzkj yktzktik zngz O gs zkyzotm cozn. Znkxk oy vatizagzout otburbkj, yotik O cgtz zu zkyz zngz oz yzorr cuxqy cozn vatizagzout.")
    if result.solution_found is True:
        print("Result: {}\nCertainty: {:.1f}%".format(result.text, result.solution_certainty*100))
    else:
        print("Did not find a solution")
