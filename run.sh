#!/bin/bash
currentDir=$(echo $(cd $(dirname $0) && pwd))
PYTHON_SITE_PACKAGES=${currentDir}/site-packages

echo ${PYTHON_SITE_PACKAGES}

# site-packagesの位置を一時的に変更する
export PYTHONPATH=$PYTHONPATH:${PYTHON_SITE_PACKAGES}
# pipでローカルインストールしたバイナリへのパスを通す
export PATH=${PYTHON_SITE_PACKAGES}/bin:$PATH

py -m pytest