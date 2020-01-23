#!/root/ysy/python/bin/python3
'''backup
Monday full backup & Other day incremental backup
'''
from time import strftime
import os
import tarfile
import hashlib
import pickle

def check_md5(fname):
    m = hashlib.md5()
    with open(fname,'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

def full_backup(src,dst,md5file):
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' % (fname,strftime('%Y%m%d'))
    fname = os.path.join(dst,fname)

    tar = tarfile.open(fname,'w:gz')
    tar.add(src)
    tar.close()

    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path,file)
            md5dict[key] = check_md5(key)

    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)

def incr_backup(src,dst,md5file):
    fname = os.path.basename(src)
    fname = '%s_incr_%s.tar.gz' % (fname,strftime('%Y%m%d'))
    fname = os.path.join(dst,fname)

    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path,file)
            md5dict[key] = check_md5(key)

    with open(md5file,'rb') as fobj:
        old_md5 = pickle.load(fobj)

    tar = tarfile.open(fname,'w:gz')
    for key in md5dict:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

    with open(md5file,'wb') as fobj:
        pickle.dump(md5file,fobj)

if __name__ == '__main__':
    src = '/root/Study/day01'
    dst = '/root/Study/day02'
    md5file = '/root/Study/day02/md5file.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst,md5file)
    else:
        incr_backup(src,dst,md5file)