# Nvidia GPU access in Docker container

Install `NVIDIA Container Toolkit` on LXC

- https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

On Docker host, testing by running bellow command

    docker run \
        --runtime=nvidia \
        --gpus all \
        --rm -it \
        nvidia/cuda:12.3.1-base-ubuntu20.04 nvidia-smi

### If host is a LXC, below error might shown

    stderr: Auto-detected mode as 'legacy' 
    nvidia-container-cli: mount error: failed to add device rules: unable to find any existing device filters attached to the cgroup: bpf_prog_query(BPF_CGROUP_DEVICE) failed: operation not permitted: unknown.

To fix, set `no-cgroups=true` inside `/etc/nvidia-container-runtime/config.toml`

## Ref
- https://docs.docker.com/engine/containers/resource_constraints/#gpu
- https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/troubleshooting.html
- https://github.com/NVIDIA/nvidia-container-toolkit/issues/139
- https://forum.proxmox.com/threads/docker-is-unable-to-access-gpu-in-lxc-gpu-passthrough.125066/
- https://www.reddit.com/r/Proxmox/comments/s0ud5y/cgroups2_problem_with_nvidiacontainercli/