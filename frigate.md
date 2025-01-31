# Frigate

Get `ffmpeg` run by Frigate

    ps -eo args | grep ffmpeg --color

Check your camera stream (video resolution, audio codec...)

    ffprobe rtsp://127.0.0.1:8554/your_stream

## Tapo 2 way audio

Ref:
- https://community.home-assistant.io/t/solved-2-way-audio-with-frigate-tapo-cameras-c320ws/793219
- https://github.com/AlexxIT/go2rtc?tab=readme-ov-file#source-tapo
