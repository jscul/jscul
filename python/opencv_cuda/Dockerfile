FROM ubuntu:20.04
LABEL maintainer="john@dogtownmedia.com"

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt upgrade
RUN apt update
RUN apt-get install -y wget

# install CUDA

RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
RUN mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
RUN apt-get -y update
RUN apt-get -y install cuda

# install opencv

RUN apt install -y build-essential cmake pkg-config unzip yasm git checkinstall
RUN apt install -y build-essential cmake pkg-config unzip yasm git checkinstall

RUN apt install -y libjpeg-dev libpng-dev libtiff-dev

RUN apt install -y libavcodec-dev libavformat-dev libswscale-dev libavresample-dev
RUN apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
RUN apt install -y libxvidcore-dev x264 libx264-dev libfaac-dev libmp3lame-dev libtheora-dev
RUN apt install -y libfaac-dev libmp3lame-dev libvorbis-dev

RUN apt install -y libopencore-amrnb-dev libopencore-amrwb-dev

RUN apt-get install -y libdc1394-22 libdc1394-22-dev libxine2-dev libv4l-dev v4l-utils
WORKDIR /usr/include/linux
RUN ln -s -f ../libv4l1-videodev.h videodev.h
WORKDIR /

RUN apt-get install -y libgtk-3-dev

RUN apt-get install -y python3-dev python3-pip
RUN pip3 install -U pip numpy
RUN apt install -y python3-testresources

RUN apt-get install -y libtbb-dev

RUN apt-get install -y libatlas-base-dev gfortran

RUN apt-get install -y libprotobuf-dev protobuf-compiler
RUN apt-get install -y libgoogle-glog-dev libgflags-dev
RUN apt-get install -y libgphoto2-dev libeigen3-dev libhdf5-dev doxygen

WORKDIR /
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/refs/tags/4.5.2.zip
RUN wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/refs/tags/4.5.2.zip
RUN unzip opencv.zip && rm -r opencv.zip
RUN unzip opencv_contrib.zip && rm -r opencv_contrib.zip

RUN pip install numpy

WORKDIR /opencv-4.5.2/build

RUN pwd
RUN ls

RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D WITH_TBB=ON \
  -D ENABLE_FAST_MATH=1 \
  -D CUDA_FAST_MATH=1 \
  -D WITH_CUBLAS=1 \
  -D WITH_CUDA=ON \
  -D BUILD_opencv_cudacodec=OFF \
  -D WITH_CUDNN=ON \
  -D OPENCV_DNN_CUDA=ON \
  -D CUDA_ARCH_BIN=7.5 \
  -D WITH_V4L=ON \
  -D WITH_QT=OFF \
  -D WITH_OPENGL=ON \
  -D WITH_GSTREAMER=ON \
  -D OPENCV_GENERATE_PKGCONFIG=ON \
  -D OPENCV_PC_FILE_NAME=opencv.pc \
  -D OPENCV_ENABLE_NONFREE=ON \
  -D OPENCV_PYTHON3_INSTALL_PATH=~/.virtualenvs/cv/lib/python3.8/site-packages \
  -D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-4.5.2/modules \
  -D INSTALL_PYTHON_EXAMPLES=OFF \
  -D INSTALL_C_EXAMPLES=OFF \
  -D BUILD_EXAMPLES=OFF ..

RUN make -j8 && make install
RUN /bin/bash -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'
RUN ldconfig
