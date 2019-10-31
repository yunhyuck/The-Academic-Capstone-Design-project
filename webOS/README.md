# WebOS Build
## 1. 최소 사양 확인

webOS 지원 버전 (OSE 1.x)
- **Raspberry Pi 3**
- **microSD card (8 GB or larger)** and microSD card reader device
- HDMI-compatible monitor and cable
- Input devices such as a keyboard and a mouse
- Ethernet cable and internet connection

운영체제
- Ubuntu 18.04 LTS (Bionic Beaver) 64-bit (Recommended)

하드웨어
* CPU
  * Minimum: Intel Core i5 dual-core with 4 threads
  * Recommended: Intel Core i7 quad-core with 8 threads or higher
+ RAM
  + Minimum: 8 GB
  + Recommended: 16 GB or higher
- Storage
  - Minimum: HDD with 100 GB of free disk space
  - Recommended: SSD with 100 GB of free disk space or more

## 2. 빌드 환경

운영체제
- Ubuntu 18.04 LTS (Bionic Beaver) 64-bit (Recommended)

하드웨어
* CPU
  * Intel Core i5 dual-core with 4 threads
+ RAM
  + 12 GB
- Storage
  - SSD with 250 GB of free disk space

## 3. 구축 

#### 1. WebOS OSE repository 복제

```
$ git clone https://github.com/webosose/build-webos.git  
$ cd build-webos
```

#### 2. 라이브러리 설치(BitBake)

```
$ sudo scripts/prerequisites.sh
```

#### 3-1. 빌드 구성
mcf 스크립트를 이용하여 빌드 구성
make, BitBake 병렬 처리 값 설정 시, -p, -b 옵션 필요.
이 때, 해당 옵션은 CPU 코어 수를 지정하게 되는데, **CPU 코어 수의 3분의 2**를 초과하지 않아야 빌드 실패를 하지 않는다.
1. CPU 수 
```
$ cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l
1
```

2. CPU 코어수
```
$ cat /proc/cpuinfo | grep "cpu cores" | uniq
cpu cores    : 2
```

**-p 및 -b 옵션 값은 *1* << (1*2) / 2 >>**

#### 3-2. 빌드 구성
```
$ ./mcf -p <number of physical CPU cores / 2> -b <number of physical CPU cores / 2> <target-device-name>
```
* raspberrypi4 (webOS OSE 2.0 이상)
* raspberrypi3 (webOS OSE 1.x 버전)
```
$ ./mcf -p 1 -b 1 raspberrypi3
```

#### 4. 이미지 구축
* webos-image : 개발 도구가없는 프로덕션 이미지
* webos-image-devel : 시스템 호출 추적기를 포함하여 다양한 개발 도구가 추가 된 이미지

```
$ source oe-init-build-env
$ bitbake webos-image
$ make webos-image
```

> 빌드 오류 발생시 진행.
```
$ unset DISTRO
$ unset MACHINE
$ unset MACHINES
```

#### 5. 이미지 빌드
```
$ source oe-init-build-env
$ bitbake webos-image-devel
```
* Raspberry Pi3 결과 이미지 생성 장소
> BUILD/deploy/images/raspberrypi3/webos-image-raspberrypi3.rootfs.rpi-sdimg.

## 3-2. 이미지 플래시
### Linux
#### 1. 위치 변경
```
$ cd <path where the image is located>
```

#### 2. microSD 카드 장치 이름 확인
```
$ sudo fdisk -l
```

#### 3. 플래시 명령어 
```
$ sudo umount /dev/<sdXn>
$ sudo dd bs=4M if=./<webOS OSE image> of=/dev/<sdX>
$ sudo umount /dev/<sdXn>
```

* 'sdXn'microSD 카드의 장치 이름
* 'sdX'파티션이 아니라 대용량 저장 장치
 
##### 플래시 예.
```
$ sudo umount /dev/sdb1
$ sudo dd bs=4M if=./webos-image-raspberrypi3.rootfs.wic of=/dev/sdb
$ sudo umount /dev/sdb1
```

<img src="https://www.webosose.org/images/docs/guides/setup/webosose-bootup-launcher.png" width="70%" height="50%" title="webOS OSE 1.x" alt="RubberDuck"></img>
