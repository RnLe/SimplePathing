# SimplePathing

A repo to somewhat understand and experiment on pathing using python.

### Packages & environment
* **python**: `3.7.6`
* **matplotlib**: used to draw shapes, animate and save video files
* **anaconda**: multiple packages like numpy, scipy etc.
* **ffmpeg**: codec used for the video files (`pip install ffmpeg-python`  **Windows**: [How to install FFmpeg for Windows](https://www.wikihow.com/Install-FFmpeg-on-Windows))

## Goals
The progression of this project sliced and grouped into several layers.

**Layer 0**  
* ~~set up environment~~

**Layer Alpha**  
* dynamic pathing class
* find (any) path to target tile

**Layer Beta**  
* find shortest path
* tile class
* tile effects
* move around blocking tiles

**Layer Gamma**  
* find fastest path
* scale gridsize
* benchmark
* simple optimizations

**Layer Hamilton**  
_without tile effects_
* multiple target tiles (given order)
* multiple target tiles (Hamiltonian Path) - _**Milestone**_  

_with tile effects_  
* Hamiltonian Path
* fastest Hamiltonian Path

**Layer Multidot**
* dot class
* second dot
* anti-colliding
  * sharing tile impairs movement
* split Hamiltonian Path
* fastest split Hamiltonian Path - _**Milestone**_  
* multiple dots

**Layer OMEGA**
* machine learning - _**Milestone**_
  * whether or not it's possible and/or effective
