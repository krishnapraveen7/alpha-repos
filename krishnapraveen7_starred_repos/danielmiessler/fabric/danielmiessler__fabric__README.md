<div align="center">

<img src="./images/fabric-logo-gif.gif" alt="fabriclogo" width="400" height="400"/>

# `fabric`

![Static Badge](https://img.shields.io/badge/mission-human_flourishing_via_AI_augmentation-purple)
<br />
![GitHub top language](https://img.shields.io/github/languages/top/danielmiessler/fabric)
![GitHub last commit](https://img.shields.io/github/last-commit/danielmiessler/fabric)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

<p class="align center">
<h4><code>fabric</code> is an open-source framework for augmenting humans using AI.</h4>
</p>

[Introduction Video](#introduction-video-by-network-chuck) •
[What and Why](#what-and-why) •
[Philosophy](#philosophy) •
[Quickstart](#quickstart) •
[Structure](#structure) •
[Examples](#examples) •
[Custom Patterns](#custom-patterns) •
[Helper Apps](#helper-apps) •
[Examples](#examples) •
[Meta](#meta)

</div>

## Navigation

- [Introduction Videos](#introduction-video-by-network-chuck)
- [What and Why](#what-and-why)
- [Philosophy](#philosophy)
  - [Breaking problems into components](#breaking-problems-into-components)
  - [Too many prompts](#too-many-prompts)
  - [The Fabric approach to prompting](#our-approach-to-prompting)
- [Quickstart](#quickstart)
  - [Setting up the fabric commands](#setting-up-the-fabric-commands)
  - [Using the fabric client](#using-the-fabric-client)
  - [Just use the Patterns](#just-use-the-patterns)
  - [Create your own Fabric Mill](#create-your-own-fabric-mill)
- [Updating](#updating)
- [Structure](#structure)
  - [Components](#components)
  - [CLI-native](#cli-native)
  - [Directly calling Patterns](#directly-calling-patterns)
- [Examples](#examples)
- [Custom Patterns](#custom-patterns)
- [Helper Apps](#helper-apps)
- [Meta](#meta)
  - [Primary contributors](#primary-contributors)

<br />

> [!NOTE]
> May 23, 2024 — We will be switching Fabric to Go in a few weeks to avoid all the installation issues with Python. The Go version will be dead-simple to install and will be even faster. Plus easier to update. We already have it working thanks to the heroic efforts of @xssdoctor, and we're just working on testing now! Stay tuned for more info on the release date!

## Introduction video by Network Chuck!

This is a **brilliant** video by Network Chuck that goes over why he's started using Fabric for all things AI. He talks about the spirit of the project, how to install it, and how he uses it, and he just generally articulates the spirit of what we're doing here SO WELL. Thanks to Chuck for this!

<div class="center">
<a href="https://youtu.be/UbDyjIIGaxQ"><img width="1000" alt="image" src="https://github.com/danielmiessler/fabric/assets/50654/a6a61885-7bb1-48d7-8ea9-777ebb2fdb94"></a>
</div>

## What and why

Since the start of 2023 and GenAI we've seen a massive number of AI applications for accomplishing tasks. It's powerful, but _it's not easy to integrate this functionality into our lives._

<div align="center">
<h4>In other words, AI doesn't have a capabilities problem—it has an <em>integration</em> problem.</h4>
</div>

Fabric was created to address this by enabling everyone to granularly apply AI to everyday challenges.

## Philosophy

> AI isn't a thing; it's a _magnifier_ of a thing. And that thing is **human creativity**.

We believe the purpose of technology is to help humans flourish, so when we talk about AI we start with the **human** problems we want to solve.

### Breaking problems into components

Our approach is to break problems into individual pieces (see below) and then apply AI to them one at a time. See below for some examples.

<img width="2078" alt="augmented_challenges" src="https://github.com/danielmiessler/fabric/assets/50654/31997394-85a9-40c2-879b-b347e4701f06">

### Too many prompts

Prompts are good for this, but the biggest challenge I faced in 2023——which still exists today—is **the sheer number of AI prompts out there**. We all have prompts that are useful, but it's hard to discover new ones, know if they are good or not, _and manage different versions of the ones we like_.

One of <code>fabric</code>'s primary features is helping people collect and integrate prompts, which we call _Patterns_, into various parts of their lives.

Fabric has Patterns for all sorts of life and work activities, including:

- Extracting the most interesting parts of YouTube videos and podcasts.
- Writing an essay in your own voice with just an idea as an input.
- Summarizing opaque academic papers.
- Creating perfectly matched AI art prompts for a piece of writing.
- Rating the quality of content to see if you want to read/watch the whole thing.
- Getting summaries of long, boring content.
- Explaining code to you.
- Turning bad documentation into usable documentation.
- Creating social media posts from any content input.
- And a million more…

### Our approach to prompting

Fabric _Patterns_ are different than most prompts you'll see.

- **First, we use `Markdown` to help ensure maximum readability and editability**. This not only helps the creator make a good one, but also anyone who wants to deeply understand what it does. _Importantly, this also includes the AI you're sending it to!_

Here's an example of a Fabric Pattern

```bash
https://github.com/danielmiessler/fabric/blob/main/patterns/extract_wisdom/system.md
```

<img width="1461" alt="pattern-example" src="https://github.com/danielmiessler/fabric/assets/50654/b910c551-9263-405f-9735-71ca69bbab6d">

- **Next, we are extremely clear in our instructions**, and we use the Markdown structure to emphasize what we want the AI to do, and in what order.

- **And finally, we tend to use the System section of the prompt almost exclusively**. In over a year of being heads-down with this stuff, we've just seen more efficacy from doing that. If that changes, or we're shown data that says otherwise, we will adjust.

## Quickstart

The most feature-rich way to use Fabric is to use the `fabric` client, which can be found under <a href="https://github.com/danielmiessler/fabric/tree/main/installer/client">`/client`</a> directory in this repository.

### Required Python Version 
Ensure you have at least python3.10 installed on your operating system. Otherwise, when you attempt to run the pip install commands, the project will fail to build due to certain dependencies. 

### Setting up the fabric commands

Follow these steps to get all fabric-related apps installed and configured.

1. Navigate to where you want the Fabric project to live on your system in a semi-permanent place on your computer.

```bash
# Find a home for Fabric
cd /where/you/keep/code
```

2. Clone the project to your computer.

```bash
# Clone Fabric to your computer
git clone https://github.com/danielmiessler/fabric.git
```

3. Enter Fabric's main directory.

```bash
# Enter the project folder (where you cloned it)
cd fabric
```

4. Install pipx:

macOS:

```bash
brew install pipx
```

Linux:

```bash
sudo apt install pipx
```

Windows:

Use WSL and follow the Linux instructions.

5. Install fabric:

```bash
pipx install .
```

6. Run setup:

```bash
fabric --setup
```

7. Restart your shell to reload everything.

8. Now you are up and running! You can test by running the help.

```bash
# Making sure the paths are set up correctly
fabric --help
```

> [!NOTE]
> If you're using the `server` functions, `fabric-api` and `fabric-webui` need to be run in distinct terminal windows.

## Updating

To update Fabric, run the following commands.

```bash
# From the fabric directory
pipx install . --force
fabric --update
```

Then restart your shell.

### Using the `fabric` client

If you want to use it with OpenAI API-compatible inference servers, such as [FastChat](https://github.com/lm-sys/FastChat), [Helmholtz Blablador](http://helmholtz-blablador.fz-juelich.de), [LM Studio](https://lmstudio.ai) and others, simply export the following environment variables:

- `export OPENAI_BASE_URL=https://YOUR-SERVER:8000/v1/`
- `export DEFAULT_MODEL="YOUR_MODEL"`

And if your server needs authentication tokens, as Blablador does, you export the token the same way you would with OpenAI:
  
- `export OPENAI_API_KEY="YOUR TOKEN"`

Once you have it all set up, here's how to use it:

1. Check out the options
   `fabric -h`

```bash
usage: fabric -h
usage: fabric [-h] [--text TEXT] [--copy] [--agents] [--output [OUTPUT]] [--session [SESSION]] [--gui] [--stream] [--list] [--temp TEMP] [--top_p TOP_P] [--frequency_penalty FREQUENCY_PENALTY]
              [--presence_penalty PRESENCE_PENALTY] [--update] [--pattern PATTERN] [--setup] [--changeDefaultModel CHANGEDEFAULTMODEL] [--model MODEL] [--listmodels]
              [--remoteOllamaServer REMOTEOLLAMASERVER] [--context]

An open-source framework for augmenting humans using AI.

options:
  -h, --help            show this help message and exit
  --text TEXT, -t TEXT  Text to extract summary from
  --copy, -C            Copy the response to the clipboard
  --agents, -a          Use praisonAI to create an AI agent and then use it. ex: 'write me a movie script'
  --output [OUTPUT], -o [OUTPUT]
                        Save the response to a file
  --session [SESSION], -S [SESSION]
                        Continue your previous conversation. Default is your previous conversation
  --gui                 Use the GUI (Node and npm need to be installed)
  --stream, -s          Use this option if you want to see the results in realtime. NOTE: You will not be able to pipe the output into another command.
  --list, -l            List available patterns
  --temp TEMP           sets the temperature for the model. Default is 0
  --top_p TOP_P         set the top_p for the model. Default is 1
  --frequency_penalty FREQUENCY_PENALTY
                        sets the frequency penalty for the model. Default is 0.1
  --presence_penalty PRESENCE_PENALTY
                        sets the presence penalty for the model. Default is 0.1
  --update, -u          Update patterns.
  --pattern PATTERN, -p PATTERN
                        The pattern (prompt) to use
  --setup               Set up your fabric instance
  --changeDefaultModel CHANGEDEFAULTMODEL
                        Change the default model. For a list of available models, use the --listmodels flag.
  --model MODEL, -m MODEL
                        Select the model to use
  --listmodels          List all available models
  --remoteOllamaServer REMOTEOLLAMASERVER
                        The URL of the remote ollamaserver to use. ONLY USE THIS if you are using a local ollama server in a non-default location or port
  --context, -c         Use Context file (context.md) to add context to your pattern
```

#### Example commands

The client, by default, runs Fabric patterns without needing a server (the Patterns were downloaded during setup). This means the client connects directly to OpenAI using the input given and the Fabric pattern used.

1. Run the `summarize` Pattern based on input from `stdin`. In this case, the body of an article.

```bash
pbpaste | fabric --pattern summarize
```

2. Run the `analyze_claims` Pattern with the `--stream` option to get immediate and streaming results.

```bash
pbpaste | fabric --stream --pattern analyze_claims
```

3. Run the `extract_wisdom` Pattern with the `--stream` option to get immediate and streaming results from any Youtube video (much like in the original introduction video).

```bash
yt --transcript https://youtube.com/watch?v=uXs-zPc63kM | fabric --stream --pattern extract_wisdom
```

4. **new** All of the patterns have been added as aliases to your bash (or zsh) config file

```bash
pbpaste | analyze_claims --stream
```

> [!NOTE]
> More examples coming in the next few days, including a demo video!

### Just use the Patterns

<img width="1173" alt="fabric-patterns-screenshot" src="https://github.com/danielmiessler/fabric/assets/50654/9186a044-652b-4673-89f7-71cf066f32d8">

<br />

If you're not looking to do anything fancy, and you just want a lot of great prompts, you can navigate to the [`/patterns`](https://github.com/danielmiessler/fabric/tree/main/patterns) directory and start exploring!

We hope that if you used nothing else from Fabric, the Patterns by themselves will make the project useful.

You can use any of the Patterns you see there in any AI application that you have, whether that's ChatGPT or some other app or website. Our plan and prediction is that people will soon be sharing many more than those we've published, and they will be way better than ours.

The wisdom of crowds for the win.

### Create your own Fabric Mill

<img width="2070" alt="fabric_mill_architecture" src="https://github.com/danielmiessler/fabric/assets/50654/ec3bd9b5-d285-483d-9003-7a8e6d842584">

<br />

But we go beyond just providing Patterns. We provide code for you to build your very own Fabric server and personal AI infrastructure!

## Structure

Fabric is themed off of, well… _fabric_—as in…woven materials. So, think blankets, quilts, patterns, etc. Here's the concept and structure:

### Components

The Fabric ecosystem has three primary components, all named within this textile theme.

- The **Mill** is the (optional) server that makes **Patterns** available.
- **Patterns** are the actual granular AI use cases (prompts).
- **Stitches** are chained together _Patterns_ that create advanced functionality (see below).
- **Looms** are the client-side apps that call a specific **Pattern** hosted by a **Mill**.

### CLI-native

One of the coolest parts of the project is that it's **command-line native**!

Each Pattern you see in the `/patterns` directory can be used in any AI application you use, but you can also set up your own server using the `/server` code and then call APIs directly!

Once you're set-up, you can do things like:

```bash
# Take any idea from `stdin` and send it to the `/write_essay` API!
echo "An idea that coding is like speaking with rules." | write_essay
```

### Directly calling Patterns

One key feature of `fabric` and its Markdown-based format is the ability to _directly reference_ (and edit) individual [Patterns](#components) directly—on their own—without any surrounding code.

As an example, here's how to call _the direct location_ of the `extract_wisdom` pattern.

```bash
https://github.com/danielmiessler/fabric/blob/main/patterns/extract_wisdom/system.md
```

This means you can cleanly, and directly reference any pattern for use in a web-based AI app, your own code, or wherever!

Even better, you can also have your [Mill](#components) functionality directly call _system_ and _user_ prompts from `fabric`, meaning you can have your personal AI ecosystem automatically kept up to date with the latest version of your favorite [Patterns](#components).

Here's what that looks like in code:

```bash
https://github.com/danielmiessler/fabric/blob/main/server/fabric_api_server.py
```

```python
# /extwis
@app.route("/extwis", methods=["POST"])
@auth_required  # Require authentication
def extwis():
    data = request.get_json()

    # Warn if there's no input
    if "input" not in data:
        return jsonify({"error": "Missing input parameter"}), 400

    # Get data from client
    input_data = data["input"]

    # Set the system and user URLs
    system_url = "https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_wisdom/system.md"
    user_url = "https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_wisdom/user.md"

    # Fetch the prompt content
    system_content = fetch_content_from_url(system_url)
    user_file_content = fetch_content_from_url(user_url)

    # Build the API call
    system_message = {"role": "system", "content": system_content}
    user_message = {"role": "user", "content": user_file_content + "\n" + input_data}
    messages = [system_message, user_message]
    try:
        response = openai.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=messages,
            temperature=0.0,
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty=0.1,
        )
        assistant_message = response.choices[0].message.content
        return jsonify({"response": assistant_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

## Examples

Here's an abridged output example from the <a href="https://github.com/danielmiessler/fabric/blob/main/patterns/extract_wisdom/system.md">`extract_wisdom`</a> pattern (limited to only 10 items per section).

```bash
# Paste in the transcript of a YouTube video of Riva Tez on David Perrel's podcast
pbpaste | extract_wisdom
```

```markdown
## SUMMARY:

The content features a conversation between two individuals discussing various topics, including the decline of Western culture, the importance of beauty and subtlety in life, the impact of technology and AI, the resonance of Rilke's poetry, the value of deep reading and revisiting texts, the captivating nature of Ayn Rand's writing, the role of philosophy in understanding the world, and the influence of drugs on society. They also touch upon creativity, attention spans, and the importance of introspection.

## IDEAS:

1. Western culture is perceived to be declining due to a loss of values and an embrace of mediocrity.
2. Mass media and technology have contributed to shorter attention spans and a need for constant stimulation.
3. Rilke's poetry resonates due to its focus on beauty and ecstasy in everyday objects.
4. Subtlety is often overlooked in modern society due to sensory overload.
5. The role of technology in shaping music and performance art is significant.
6. Reading habits have shifted from deep, repetitive reading to consuming large quantities of new material.
7. Revisiting influential books as one ages can lead to new insights based on accumulated wisdom and experiences.
8. Fiction can vividly illustrate philosophical concepts through characters and narratives.
9. Many influential thinkers have backgrounds in philosophy, highlighting its importance in shaping reasoning skills.
10. Philosophy is seen as a bridge between theology and science, asking questions that both fields seek to answer.

## QUOTES:

1. "You can't necessarily think yourself into the answers. You have to create space for the answers to come to you."
2. "The West is dying and we are killing her."
3. "The American Dream has been replaced by mass-packaged mediocrity porn, encouraging us to revel like happy pigs in our own meekness."
4. "There's just not that many people who have the courage to reach beyond consensus and go explore new ideas."
5. "I'll start watching Netflix when I've read the whole of human history."
6. "Rilke saw beauty in everything... He sees it's in one little thing, a representation of all things that are beautiful."
7. "Vanilla is a very subtle flavor... it speaks to sort of the sensory overload of the modern age."
8. "When you memorize chapters [of the Bible], it takes a few months, but you really understand how things are structured."
9. "As you get older, if there's books that moved you when you were younger, it's worth going back and rereading them."
10. "She [Ayn Rand] took complicated philosophy and embodied it in a way that anybody could resonate with."

## HABITS:

1. Avoiding mainstream media consumption for deeper engagement with historical texts and personal research.
2. Regularly revisiting influential books from youth to gain new insights with age.
3. Engaging in deep reading practices rather than skimming or speed-reading material.
4. Memorizing entire chapters or passages from significant texts for better understanding.
5. Disengaging from social media and fast-paced news cycles for more focused thought processes.
6. Walking long distances as a form of meditation and reflection.
7. Creating space for thoughts to solidify through introspection and stillness.
8. Embracing emotions such as grief or anger fully rather than suppressing them.
9. Seeking out varied experiences across different careers and lifestyles.
10. Prioritizing curiosity-driven research without specific goals or constraints.

## FACTS:

1. The West is perceived as declining due to cultural shifts away from traditional values.
2. Attention spans have shortened due to technological advancements and media consumption habits.
3. Rilke's poetry emphasizes finding beauty in everyday objects through detailed observation.
4. Modern society often overlooks subtlety due to sensory overload from various stimuli.
5. Reading habits have evolved from deep engagement with texts to consuming large quantities quickly.
6. Revisiting influential books can lead to new insights based on accumulated life experiences.
7. Fiction can effectively illustrate philosophical concepts through character development and narrative arcs.
8. Philosophy plays a significant role in shaping reasoning skills and understanding complex ideas.
9. Creativity may be stifled by cultural nihilism and protectionist attitudes within society.
10. Short-term thinking undermines efforts to create lasting works of beauty or significance.

## REFERENCES:

1. Rainer Maria Rilke's poetry
2. Netflix
3. Underworld concert
4. Katy Perry's theatrical performances
5. Taylor Swift's performances
6. Bible study
7. Atlas Shrugged by Ayn Rand
8. Robert Pirsig's writings
9. Bertrand Russell's definition of philosophy
10. Nietzsche's walks
```

## Custom Patterns

You can also use Custom Patterns with Fabric, meaning Patterns you keep locally and don't upload to Fabric.

One possible place to store them is `~/.config/custom-fabric-patterns`. 

Then when you want to use them, simply copy them into `~/.config/fabric/patterns`.

```bash
cp -a ~/.config/custom-fabric-patterns/* ~/.config/fabric/patterns/
```

Now you can run them with:

```bash
pbpaste | fabric -p your_custom_pattern
```

## Agents

NEW FEATURE! We have incorporated [PraisonAI](https://github.com/MervinPraison/PraisonAI) into Fabric. This feature creates AI agents and then uses them to perform a task.

```bash
echo "Search for recent articles about the future of AI and write me a 500-word essay on the findings" | fabric --agents
```

This feature works with all OpenAI and Ollama models but does NOT work with Claude. You can specify your model with the -m flag.

For more information about this amazing project, please visit https://github.com/MervinPraison/PraisonAI.

## Helper Apps

These are helper tools to work with Fabric. Examples include things like getting transcripts from media files, getting metadata about media, etc.

## yt (YouTube)

`yt` is a command that uses the YouTube API to pull transcripts, pull user comments, get video duration, and other functions. It's primary function is to get a transcript from a video that can then be stitched (piped) into other Fabric Patterns.

```bash
usage: yt [-h] [--duration] [--transcript] [url]

vm (video meta) extracts metadata about a video, such as the transcript and the video's duration. By Daniel Miessler.

positional arguments:
  url           YouTube video URL

options:
  -h, --help    Show this help message and exit
  --duration    Output only the duration
  --transcript  Output only the transcript
  --comments    Output only the user comments
```

## ts (Audio transcriptions)

'ts' is a command that uses the OpenAI Whisper API to transcribe audio files. Due to the context window, this tool uses pydub to split the files into 10 minute segments. for more information on pydub, please refer https://github.com/jiaaro/pydub

### Installation

```bash

mac:
brew install ffmpeg

linux:
apt install ffmpeg

windows:
download instructions https://www.ffmpeg.org/download.html
```

```bash
ts -h
usage: ts [-h] audio_file

Transcribe an audio file.

positional arguments:
  audio_file  The path to the audio file to be transcribed.

options:
  -h, --help  show this help message and exit
```

## Save

`save` is a "tee-like" utility to pipeline saving of content, while keeping the output stream intact. Can optionally generate "frontmatter" for PKM utilities like Obsidian via the
"FABRIC_FRONTMATTER" environment variable

If you'd like to default variables, set them in `~/.config/fabric/.env`. `FABRIC_OUTPUT_PATH` needs to be set so `save` where to write. `FABRIC_FRONTMATTER_TAGS` is optional, but useful for tracking how tags have entered your PKM, if that's important to you.

### usage

```bash
usage: save [-h] [-t, TAG] [-n] [-s] [stub]

save: a "tee-like" utility to pipeline saving of content, while keeping the output stream intact. Can optionally generate "frontmatter" for PKM utilities like Obsidian via the
"FABRIC_FRONTMATTER" environment variable

positional arguments:
  stub                stub to describe your content. Use quotes if you have spaces. Resulting format is YYYY-MM-DD-stub.md by default

options:
  -h, --help          show this help message and exit
  -t, TAG, --tag TAG  add an additional frontmatter tag. Use this argument multiple timesfor multiple tags
  -n, --nofabric      don't use the fabric tags, only use tags from --tag
  -s, --silent        don't use STDOUT for output, only save to the file
```

### Example

```bash
echo test | save --tag extra-tag stub-for-name
test

$ cat ~/obsidian/Fabric/2024-03-02-stub-for-name.md
---
generation_date: 2024-03-02 10:43
tags: fabric-extraction stub-for-name extra-tag
---
test
```

## Meta

> [!NOTE]
> Special thanks to the following people for their inspiration and contributions!

- _Caleb Sima_ for pushing me over the edge of whether to make this a public project or not.
- _Joel Parish_ for super useful input on the project's Github directory structure.
- _Jonathan Dunn_ for spectacular work on the soon-to-be-released universal client.
- _Joseph Thacker_ for the idea of a `-c` context flag that adds pre-created context in the `./config/fabric/` directory to all Pattern queries.
- _Jason Haddix_ for the idea of a stitch (chained Pattern) to filter content using a local model before sending on to a cloud model, i.e., cleaning customer data using `llama2` before sending on to `gpt-4` for analysis.
- _Dani Goland_ for enhancing the Fabric Server (Mill) infrastructure by migrating to FastAPI, breaking the server into discrete pieces, and Dockerizing the entire thing.
- _Andre Guerra_ for simplifying installation by getting us onto Poetry for virtual environment and dependency management.

### Primary contributors

<a href="https://github.com/danielmiessler"><img src="https://avatars.githubusercontent.com/u/50654?v=4" title="Daniel Miessler" width="50" height="50"></a>
<a href="https://github.com/xssdoctor"><img src="https://avatars.githubusercontent.com/u/9218431?v=4" title="Jonathan Dunn" width="50" height="50"></a>
<a href="https://github.com/sbehrens"><img src="https://avatars.githubusercontent.com/u/688589?v=4" title="Scott Behrens" width="50" height="50"></a>
<a href="https://github.com/agu3rra"><img src="https://avatars.githubusercontent.com/u/10410523?v=4" title="Andre Guerra" width="50" height="50"></a>

`fabric` was created by <a href="https://danielmiessler.com/subscribe" target="_blank">Daniel Miessler</a> in January of 2024.
<br /><br />
<a href="https://twitter.com/intent/user?screen_name=danielmiessler">![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/danielmiessler)</a>
