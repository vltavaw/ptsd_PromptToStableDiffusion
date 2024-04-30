## ptsd_PromptToStableDiffusion

### Introduction
For users without a CS background, producing high-quality prompts can be difficult. Below demonstrates what an untrained user might write as a prompt(first image), compared to an optimized propmpt about what they might actually want to generate(second image).
![image](https://drive.google.com/uc?id=1tmSdp2AG2KP5gY6i98rYxJd0CAYu6zla)

In this project we aim to answer the following questions:
1. Can prompting techniques help improve image generation quality?
2. Can we use (improved prompting, image) pairs as training data, to in turn improve text-to-image generation models?

### Team Members
Blake Wang (bw669)

Vicky Yue (wy164)

### Related Work and Repositories
*InstanceDiffusion* demonstrates an instance-level control for Image Generation by breaking down the captions into instance-level captions.

OpenAI *DALL-E* and *Sora* demonstrates the power of using Large Language Models to convert the short user input into a long, detailed prompt for the text-to-image genration model.

We also explored several papers regarding how to generate better prompts(see references).

We followed some huggingface tutorials on training and evaluating(and of course the assignments!) and used their scripts for train on a small subset of coco. 

Links:

https://github.com/huggingface/diffusers/blob/main/examples/text_to_image/README.md

https://huggingface.co/docs/diffusers/en/conceptual/evaluation

### How to Run
We provide a demo.ipynb to demonstrate our pipeline because the main file is a bit messy with all sorts of attempts we tried(some on gdrive, some on local). We load the models from huggingface so a token is required to run the demo, you will also need to download the two demo images in the `/demo` folder and put it into your drive, to see the results. Please note that this is only for showing that our solution works with 2 demo images since it's not possible to upload the entire dataset, so the results may vary.

We followed this huggingface tutorial on training, and used their scripts for train on a small subset of coco.
https://github.com/huggingface/diffusers/blob/main/examples/text_to_image/README.md


### References

Sora Technical Report: Video generation models as world simulators, https://openai.com/research/video-generation-models-as-world-simulators.

InstanceDiffusion: Instance-level Control for Image Generation, arxiv 2402.03290.

PromptCrafter: Crafting Text-to-Image Prompt through Mixed-Initiative Dialogue with LLM, arxiv 2307.08985.

Optimizing Prompts for Text-to-Image Generation, arxiv 2212.09611.

Improving Text-to-Image Consistency via Automatic Prompt Optimization, arxiv 2403.17804.

### Slides
https://docs.google.com/presentation/d/19FW8rNYkOIZBo3WhzXp_AhszTWkOuMj_lsNe4IySYT8/edit?usp=sharing

View access is for GU accounts only. Alternatively if the link is not working, there is a copy of our .pptx in this repo.
