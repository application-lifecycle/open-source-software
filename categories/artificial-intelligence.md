# Open source artificial intelligence software

Local AI runtimes, inference servers, and self-hosted chat interfaces let individuals and organizations run open-weight language, speech, and image models on their own hardware without sending data to external APIs.

[Back to main catalog](../README.md)

## Comparison table

<!-- START:CATEGORY_TABLE -->
| Software | Alternative to | Platform | License | Stars | Last release | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Ollama](https://ollama.com/) | OpenAI API, LM Studio | Win, Mac, Linux | MIT | 188.1k | 2026-11-24 | Active | Low | Running open-weight LLMs locally via CLI and HTTP API |
| [Open WebUI](https://openwebui.com/) | ChatGPT Web UI | Web | Open WebUI License (BSD-3-Clause based) * | 159.5k | 2026-11-25 | Active | Low | Self-hosted chat interface for Ollama and OpenAI-compatible APIs |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Proprietary LLM runtimes | Win, Mac, Linux | MIT | 136.2k | 2026-11-13 | Active | Medium | Low-overhead C/C++ inference for quantized GGUF models |
| [vLLM](https://vllm.ai/) | Proprietary LLM serving platforms | Linux | Apache-2.0 | 97.6k | 2026-11-16 | Active | Medium | High-throughput GPU model serving with PagedAttention |
| [ComfyUI](https://www.comfy.org/) | Midjourney, Adobe Firefly | Win, Mac, Linux, Web | GPL-3.0 | 148.6k | 2026-11-18 | Active | Medium | Node-based image and video diffusion workflows |
| [LocalAI](https://localai.io/) | OpenAI API | Linux, Mac, Win | MIT | 50.5k | 2026-11-20 | Active | Low | Drop-in local REST API for text, audio, and image models |
| [AnythingLLM](https://anythingllm.com/) | ChatGPT Team, Custom GPTs | Win, Mac, Linux, Web | MIT | 68.6k | 2026-11-17 | Active | Low | Desktop and server RAG workspaces over local documents |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Commercial speech-to-text APIs | Win, Mac, Linux | MIT | 55.5k | 2026-11-23 | Active | Low | Fast offline audio transcription on CPU or Apple Silicon |
<!-- END:CATEGORY_TABLE -->

## Choosing a local AI stack

- On a laptop, install Ollama for model management and pair it with Open WebUI when you want a browser chat interface with document uploads.
- On Linux GPU servers, use vLLM for continuous batching and high concurrent throughput.
- For CPU and edge inference, use llama.cpp for quantized GGUF text models and whisper.cpp for offline speech-to-text transcription.
- AnythingLLM bundles workspace permissions and vector storage in a desktop app or Docker container for team document Q&A.
- ComfyUI exposes every step of an image or video diffusion pipeline as a reproducible node graph.
