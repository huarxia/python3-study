#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-11 11:01:25
# @Author  : 花夏 (liubiao@itoxs.com)
# @Link    : https://github.com/huarxia
# @Version : 1.0.0

import os,sys

result = []

def get_all (cwd, suffixName):
    """
        获取所有需要复制的路径
    """

    # 遍历当前目录，获取文件列表
    get_dir = os.listdir(cwd)

    for i in get_dir:
        # 把第一步获取的文件加入路径
        sub_dir = os.path.join(cwd,i)
        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir, suffixName)
        elif os.path.splitext(i)[1] == suffixName:
            # 如果当前路径不是文件夹且符合后缀名，则把文件名放入列表
            # ax = os.path.basename(sub_dir)

            # 把文件名的当前路径放入列表
            result.append(sub_dir)
            # 对列表计数
            print(len(result))

def copy_video (localDir = os.getcwd(), suffixName = '.mp4', *destinationDir):
    """
        复制视频主函数

        localDir: 设置需要复制的目录，默认使用当前脚本目录， os.getcwd()
        suffixName: 复制文件的后缀名，默认MP4
        destinationDir: 复制的目的地文件夹 可选参数
    """
    print('复制问文件夹是-->' + localDir)
    destinationDir = localDir + '/' + destinationDir[0]
    if (destinationDir and not(os.path.isdir(destinationDir[0]))):
        destinationDir = localDir + '/' + destinationDir[0]
        os.mkdir(destinationDir)

    get_all(localDir, suffixName)
    for i in result:
        # print(i)
        os.system('cp ' + i + ' ' + destinationDir)

if __name__ == '__main__':
    local = '/Users/huaxia/macsoft'
    copy_video(local, '.avi', '123')
    print(local + '目录下目标文建，复制完毕!!!')
