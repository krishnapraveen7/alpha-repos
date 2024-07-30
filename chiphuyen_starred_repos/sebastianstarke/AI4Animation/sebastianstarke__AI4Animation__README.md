# [AI4Animation](https://github.com/sebastianstarke/AI4Animation)

AI4Animation: Deep Learning for Character Control
============

This repository explores the opportunities of deep learning for character animation and control. It aims to be a comprehensive framework for data-driven character animation, including data processing, neural network training and runtime control, developed in Unity3D / PyTorch. The various projects below demonstrate such capabilities using neural networks for animating biped locomotion, quadruped locomotion, and character-scene interactions with objects and the environment, plus sports and fighting games, as well as embodied avatar motions in AR/VR. Further advances on this research will continue being added to this project.

------------
**SIGGRAPH 2024**<br />
**Categorical Codebook Matching for Embodied Character Controllers**<br >
<sub>
<a href="https://www.linkedin.com/in/sebastian-starke-b281a6148/">Sebastian Starke</a>, 
<a href="https://www.linkedin.com/in/paul-starke-0787211b4/">Paul Starke</a>, 
<a href="https://www.linkedin.com/in/nicky-sijia-he-92240590/">Nicky He</a>, 
<a href="https://www.linkedin.com/in/taku-komura-571b32b/">Taku Komura</a>,
<a href="https://www.linkedin.com/in/yuting-ye-77a75332/">Yuting Ye</a>, 
ACM Trans. Graph. 43, 4, Article 142.
<sub>
------------
<img src ="Media/SIGGRAPH_2024/Teaser.png" width="100%">


<p align="center">
Translating motions from a real user onto a virtual embodied avatar is a key challenge for character animation in the metaverse. In this work, we present a novel generative framework that enables mapping from a set of sparse sensor signals to a full body avatar motion in real-time while faithfully preserving the motion context of the user. In contrast to existing techniques that require training a motion prior and its mapping from control to motion separately, our framework is able to learn the motion manifold as well as how to sample from it at the same time in an end-to-end manner. To achieve that, we introduce a technique called codebook matching which matches the probability distribution between two categorical codebooks for the inputs and outputs for synthesizing the character motions. We demonstrate this technique can successfully handle ambiguity in motion generation and produce high quality character controllers from unstructured motion capture data. Our method is especially useful for interactive applications like virtual reality or video games where high accuracy and responsiveness are needed.
</p>


<p align="center" style="font-size:1.25em;">
-
<a href="https://youtu.be/NyLRcY0c0p4">Video</a>
-
<a href="Media/SIGGRAPH_2024/Paper.pdf">Paper</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2024/Cranberry_Dataset.zip">Dataset</a>
-
<a href="AI4Animation/SIGGRAPH_2024/">Code</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2024/VR Demo.zip">VR Demo</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2024/Demo_Win.zip">Windows Demo</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2024/Demo_Mac.zip">Mac Demo</a>
-
<a href="AI4Animation/SIGGRAPH_2024/ReadMe.md">ReadMe</a>
-
</p>

<img src ="Media/SIGGRAPH_2024/Architecture.png">


Unlike existing methods for kinematic character control that learn a direct mapping between inputs and outputs or utilize a motion prior that is trained on the motion data alone, our framework learns from both the inputs and outputs simultaneously to form a motion manifold that is informed about the control signals.
To learn such setup in a supervised manner, we propose a technique that we call Codebook Matching which enforces similarity
between both latent probability distributions $Z_𝑋$ and $Z_𝑌$.
In the context of motion generation, instead of directly predicting the motions outputs from the control inputs, we only predict their probabilities for each of them to appear.
By introducing a matching loss between both categorical probability distributions, our codebook matching technique allows to substitute $Z_𝑌$ by $Z_𝑋$ during test time.

```math
Training:
\begin{cases}
    Y \rightarrow Z_Y \rightarrow Y
    \\
    X \rightarrow Z_X
    \\
    Z_X \sim Z_Y
\end{cases}

Inference: 
X \rightarrow Z_X \rightarrow Y
```

Our method is not limited to three-point inputs but we can also use it to generate embodied character movements with additional joystick or button controls by what we call hybrid control mode. In this setting, the user, engineer or artist can additionally tell the character where to go via a simple goal location while preserving the original context of motion from three-point tracking signals. This changes the scope of applications we can address by walking / running / crouching in the virtual world while standing or even sitting in the real world.

<img src ="Media/SIGGRAPH_2024/Collection.png">

Furthermore, our codebook matching architecture shares many similarities with motion matching and is able to learn a similar structure in an end-to-end manner. While motion matching can bypass ambiguity in the mapping from control to motion by selecting among candidates with similar query distances, our setup selects possible outcomes from predicted probabilities and naturally projects against valid output motions if their probabilities are similar. However, in contrast to database searches, our codebook matching is able to effectively compress the motion data where same motions map to same codes, and can bypass ambiguity issues which existing learning-based methods such as standard feed-forward networks (MLP) or variational models (CVAE) may struggle with. We demonstrate such capabilities by reconstructing the ambiguous toy example functions in the figure below.

<img src ="Media/SIGGRAPH_2024/ToyExample.png">

<p align="center">
    <a href="https://youtu.be/NyLRcY0c0p4">
    <img src="Media/SIGGRAPH_2024/Thumbnail.png", width=100%>
    </a>
</p>

------------
**SIGGRAPH 2022**<br />
**DeepPhase: Periodic Autoencoders for Learning Motion Phase Manifolds**<br >
<sub>
<a href="https://www.linkedin.com/in/sebastian-starke-b281a6148/">Sebastian Starke</a>, 
<a href="https://www.linkedin.com/in/ian-mason-134197105/">Ian Mason</a>, 
<a href="https://www.linkedin.com/in/taku-komura-571b32b/">Taku Komura</a>, 
ACM Trans. Graph. 41, 4, Article 136.
<sub>
------------
<img src ="Media/SIGGRAPH_2022/Teaser.png" width="100%">

<p align="center">
Learning the spatial-temporal structure of body movements is a fundamental problem for character motion synthesis. In this work, we propose a novel neural network architecture called the Periodic Autoencoder that can learn periodic features from large unstructured motion datasets in an unsupervised manner. The character movements are decomposed into multiple latent channels that capture the non-linear periodicity of different body segments while progressing forward in time. Our method extracts a multi-dimensional phase space from full-body motion data, which effectively clusters animations and produces a manifold in which computed feature distances provide a better similarity measure than in the original motion space to achieve better temporal and spatial alignment. We demonstrate that the learned periodic embedding can significantly help to improve neural motion synthesis in a number of tasks, including diverse locomotion skills, style-based movements, dance motion synthesis from music, synthesis of dribbling motions in football, and motion query for matching poses within large animation databases.
</p>

<p align="center">
<img src ="Media/SIGGRAPH_2022/Manifolds.png" width="100%">
</p>

<p align="center">
-
<a href="https://www.youtube.com/watch?v=YhH4PYEkVnY">Video</a>
-
<a href="Media/SIGGRAPH_2022/Paper.pdf">Paper</a>
-
<a href="AI4Animation/SIGGRAPH_2022/PyTorch">PAE Code & Demo</a>
-
<a href="AI4Animation/SIGGRAPH_2022/Unity">Animation Code & Demo</a>
-
<a href="https://www.ianxmason.com/posts/PAE/">Explanation and Addendum</a>
-
<a href="https://youtu.be/3ASGrxNDd0k">Tutorial</a>
-
</p>

<p align="left">
    <a href="https://www.youtube.com/watch?v=YhH4PYEkVnY">
    <img  width="47%" src="Media/SIGGRAPH_2022/Thumbnail.png">
    </a>
    <a href="https://www.youtube.com/watch?v=3ASGrxNDd0k">
    <img align="right" width="47%" src="Media/SIGGRAPH_2022/PAEthumbnail.png">
    </a>
</p>

<p align="center">
-
<a href="https://github.com/pauzii/PhaseBetweener">Motion In-Betweening System</a>
-
</p>
<img src ="https://github.com/pauzii/PhaseBetweener/raw/main/Media/Teaser.png" width="100%">

------------
**SIGGRAPH 2021**<br />
**Neural Animation Layering for Synthesizing Martial Arts Movements**<br >
<sub>
<a href="https://www.linkedin.com/in/sebastian-starke-b281a6148/">Sebastian Starke</a>, 
<a href="https://www.linkedin.com/in/evan-yiwei-zhao-18584a105/">Yiwei Zhao</a>, 
<a href="https://www.linkedin.com/in/fabio-zinno-1a77331/">Fabio Zinno</a>, 
<a href="https://www.linkedin.com/in/taku-komura-571b32b/">Taku Komura</a>, 
ACM Trans. Graph. 40, 4, Article 92.
<sub>
------------
<img src ="Media/SIGGRAPH_2021/Teaser.jpg" width="100%">

<p align="center">
<img src ="Media/SIGGRAPH_2021/Layering.png" width="80%">
</p>

<p align="center">
Interactively synthesizing novel combinations and variations of character movements from different motion skills is a key problem in computer animation. In this research, we propose a deep learning framework to produce a large variety of martial arts movements in a controllable manner from raw motion capture data. Our method imitates animation layering using neural networks with the aim to overcome typical challenges when mixing, blending and editing movements from unaligned motion sources. The system can be used for offline and online motion generation alike, provides an intuitive interface to integrate with animator workflows, and is relevant for real-time applications such as computer games.
</p>

<p align="center">
-
<a href="https://www.youtube.com/watch?v=SkJNxLYNwN0">Video</a>
-
<a href="Media/SIGGRAPH_2021/Paper.pdf">Paper</a>
-
</p>

<p align="center">
<a href="https://www.youtube.com/watch?v=SkJNxLYNwN0">
<img width="60%" src="Media/SIGGRAPH_2021/Thumbnail.jpg">
</a>
</p>

------------
**SIGGRAPH 2020**<br />
**Local Motion Phases for Learning Multi-Contact Character Movements**<br >
<sub>
<a href="https://www.linkedin.com/in/sebastian-starke-b281a6148/">Sebastian Starke</a>, 
<a href="https://www.linkedin.com/in/evan-yiwei-zhao-18584a105/">Yiwei Zhao</a>, 
<a href="https://www.linkedin.com/in/taku-komura-571b32b/">Taku Komura</a>, 
<a href="https://www.linkedin.com/in/kazizaman/">Kazi Zaman</a>.
ACM Trans. Graph. 39, 4, Article 54.
<sub>
------------
<img src ="Media/SIGGRAPH_2020/Teaser.png" width="100%">

<p align="center">
Not sure how to align complex character movements? Tired of phase labeling? Unclear how to squeeze everything into a single phase variable? Don't worry, a solution exists!
</p>
<p align="center">
<img src ="Media/SIGGRAPH_2020/Court.jpg" width="60%">
</p>

<p align="center">
Controlling characters to perform a large variety of dynamic, fast-paced and quickly changing movements is a key challenge in character animation. In this research, we present a deep 
learning framework to interactively synthesize such animations in high quality, both from unstructured motion data and without any manual labeling. We introduce the concept of local 
motion phases, and show our system being able to produce various motion skills, such as ball dribbling and professional maneuvers in basketball plays, shooting, catching, avoidance, 
multiple locomotion modes as well as different character and object interactions, all generated under a unified framework.
</p>

<p align="center">
-
<a href="https://www.youtube.com/watch?v=Rzj3k3yerDk">Video</a>
-
<a href="Media/SIGGRAPH_2020/Paper.pdf">Paper</a>
-
<a href="AI4Animation/SIGGRAPH_2020">Code</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2020/Demo_Windows.zip">Windows Demo</a>
-
<a href="AI4Animation/SIGGRAPH_2020/ReadMe.md">ReadMe</a>
-
</p>

<p align="center">
<a href="https://www.youtube.com/watch?v=Rzj3k3yerDk">
<img width="60%" src="Media/SIGGRAPH_2020/Thumbnail.jpg">
</a>
</p>

------------
**SIGGRAPH Asia 2019**<br />
**Neural State Machine for Character-Scene Interactions**<br >
<sub>
<a href="https://www.linkedin.com/in/sebastian-starke-b281a6148/">Sebastian Starke</a><sup>+</sup>, 
<a href="https://www.linkedin.com/in/he-zhang-148467165/">He Zhang</a><sup>+</sup>, 
<a href="https://www.linkedin.com/in/taku-komura-571b32b/">Taku Komura</a>, 
<a href="https://www.linkedin.com/in/jun-saito/">Jun Saito</a>. 
ACM Trans. Graph. 38, 6, Article 178.
</sub><br /><sub><sup>(+Joint First Authors)</sup>
<sub>
------------
<img src ="Media/SIGGRAPH_Asia_2019/Teaser.jpg" width="100%">

<p align="center">
Animating characters can be an easy or difficult task - interacting with objects is one of the latter.
In this research, we present the Neural State Machine, a data-driven deep learning framework for character-scene interactions. The difficulty in such animations is that they require complex planning of periodic as well as aperiodic movements to complete a given task. Creating them in a production-ready quality is not straightforward and often very time-consuming. Instead, our system can synthesize different movements and scene interactions from motion capture data, and allows the user to seamlessly control the character in real-time from simple control commands. Since our model directly learns from the geometry, the motions can naturally adapt to variations in the scene. We show that our system can generate a large variety of movements, icluding locomotion, sitting on chairs, carrying boxes, opening doors and avoiding obstacles, all from a single model. The model is responsive, compact and scalable, and is the first of such frameworks to handle scene interaction tasks for data-driven character animation.
</p>

<p align="center">
-
<a href="https://www.youtube.com/watch?v=7c6oQP1u2eQ">Video</a>
-
<a href="Media/SIGGRAPH_Asia_2019/Paper.pdf">Paper</a>
-
<a href="AI4Animation/SIGGRAPH_Asia_2019">Code & Demo</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_Asia_2019/MotionCapture.zip">Mocap Data</a>
-
<a href="AI4Animation/SIGGRAPH_Asia_2019/ReadMe.md">ReadMe</a>
-
</p>

<p align="center">
<a href="https://www.youtube.com/watch?v=7c6oQP1u2eQ">
<img width="60%" src="Media/SIGGRAPH_Asia_2019/Thumbnail.jpg">
</a>
</p>

------------
**SIGGRAPH 2018**<br />
**Mode-Adaptive Neural Networks for Quadruped Motion Control**<br >
<sub>
<a href="https://www.linkedin.com/in/he-zhang-148467165/">He Zhang</a><sup>+</sup>, 
<a href="https://www.linkedin.com/in/sebastian-starke-b281a6148/">Sebastian Starke</a><sup>+</sup>, 
<a href="https://www.linkedin.com/in/taku-komura-571b32b/">Taku Komura</a>, 
<a href="https://www.linkedin.com/in/jun-saito/">Jun Saito</a>. 
ACM Trans. Graph. 37, 4, Article 145.
</sub><br /><sub><sup>(+Joint First Authors)</sup>
<sub>
------------
<img src ="Media/SIGGRAPH_2018/Teaser.png" width="100%">

<p align="center">
Animating characters can be a pain, especially those four-legged monsters!
This year, we will be presenting our recent research on quadruped animation and character control at the SIGGRAPH 2018 in Vancouver. The system can produce natural animations from real motion data using a novel neural network architecture, called Mode-Adaptive Neural Networks. Instead of optimising a fixed group of weights, the system learns to dynamically blend a group of weights into a further neural network, based on the current state of the character. That said, the system does not require labels for the phase or locomotion gaits, but can learn from unstructured motion capture data in an end-to-end fashion.
</p>

<p align="center">
-
<a href="https://www.youtube.com/watch?v=uFJvRYtjQ4c">Video</a>
-
<a href="Media/SIGGRAPH_2018/Paper.pdf">Paper</a>
-
<a href="AI4Animation/SIGGRAPH_2018">Code</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2018/MotionCapture.zip">Mocap Data</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2018/Demo_Windows.zip">Windows Demo</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2018/Demo_Linux.zip">Linux Demo</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2018/Demo_Mac.zip">Mac Demo</a>
-
<a href="AI4Animation/SIGGRAPH_2018/ReadMe.md">ReadMe</a>
-
</p>

<p align="center">
<a href="https://www.youtube.com/watch?v=uFJvRYtjQ4c">
<img width="60%" src="Media/SIGGRAPH_2018/Thumbnail.png">
</a>
</p>


<p align="center">
-
<a href="https://github.com/pauzii/AnimationAuthoring">Animation Authoring Tool</a>
-
</p>
<img src ="https://github.com/pauzii/AnimationAuthoring/raw/main/Media/Teaser.png" width="100%">

------------
**SIGGRAPH 2017**<br />
**Phase-Functioned Neural Networks for Character Control**<br >
<sub>
<a href="https://www.linkedin.com/in/daniel-holden-300b871b/">Daniel Holden</a>,
<a href="https://www.linkedin.com/in/taku-komura-571b32b/">Taku Komura</a>, 
<a href="https://www.linkedin.com/in/jun-saito/">Jun Saito</a>. 
ACM Trans. Graph. 36, 4, Article 42.
</sub>
------------
<img src ="Media/SIGGRAPH_2017/Adam.png" width="100%">

<p align="center">
This work continues the recent work on PFNN (Phase-Functioned Neural Networks) for character control.
A demo in Unity3D using the original weights for terrain-adaptive locomotion is contained in the Assets/Demo/SIGGRAPH_2017/Original folder.
Another demo on flat ground using the Adam character is contained in the Assets/Demo/SIGGRAPH_2017/Adam folder.
In order to run them, you need to download the neural network weights from the link provided in the Link.txt file, extract them into the /NN folder, 
and store the parameters via the custom inspector button.
</p>

<p align="center">
-
<a href="https://www.youtube.com/watch?v=Ul0Gilv5wvY">Video</a>
-
<a href="http://theorangeduck.com/media/uploads/other_stuff/phasefunction.pdf">Paper</a>
-
<a href="AI4Animation/SIGGRAPH_2017">Code (Unity)</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2017/Demo_Windows.zip">Windows Demo</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2017/Demo_Linux.zip">Linux Demo</a>
-
<a href="https://starke-consult.de/AI4Animation/SIGGRAPH_2017/Demo_Mac.zip">Mac Demo</a>
-
</p>

<p align="center">
<a href="https://www.youtube.com/watch?v=Ul0Gilv5wvY">
<img width="60%" src="https://img.youtube.com/vi/Ul0Gilv5wvY/0.jpg">
</a>
</p>

------------

Thesis Fast Forward Presentation from SIGGRAPH 2020
============
<p align="center">
<a href="https://www.youtube.com/watch?v=wNqpSk4FhSw">
<img width="100%" src="Media/Other/ThesisFastForward.jpg">
</a>
</p>

Copyright Information
============
This project is only for research or education purposes, and not freely available for commercial use or redistribution. The motion capture data is available only under the terms of the [Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode) (CC BY-NC 4.0) license.
