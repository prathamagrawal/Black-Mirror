# :art:&nbsp; Black Mirror

<details open="open">
  <summary><h3 dir="auto"><a id="user-content-table-of-contents" class="anchor" aria-hidden="true" href="#table-of-contents"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Table of Contents</h3></summary>
  <ol dir="auto">
    <li><a href="#-About">About</a>
      <ul dir="auto">
        <li><a href="#-Working">Working</a></li>
        <li><a href="#-tech-stack">Tech Stack</a></li>
      </ul>
    </li>
    <li>
      <a href="#-getting-started">Getting Started</a>
      <ul dir="auto">
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>

### :computer: &nbsp; About
<hr />
Black Mirror is an application that aims to create a model that takes a grayscale (black and white) image as input and then produces a visually plausible and perceptually meaningful colorized output image as output. We use a CNN model to map colors to Lab Colors space. 
After Colorisation, the image is subjected to different image enchancement techniques such as image sharpening and histogram equalization. 

The entire process can be summarised as follows:
1. Use the L channel as the input to the network and train the network to predict the ab channels.
2. Combine the input L channel with the predicted ab channels.
3. Convert the Lab image back to RGB.
4. Enchance Image using different techniques. 
   
### :hammer_and_wrench: &nbsp; Working
<hr />
1. Landing/Upload Page
2. Results Page

### :keyboard: &nbsp; Tech Stack
<ul dir="auto">
<li><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png"><img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" height="32" style="max-width: 100%;"></a> Python</li>
<li><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png"><img src="https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png" height="32" style="max-width: 100%;"></a> Flask</li>
<li><a target="_blank" rel="noopener noreferrer nofollow" href="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg"><img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" height="32" style="max-width: 100%;"></a> Tensorflow</li>
<li><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png"><img src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png" height="32" style="max-width: 100%;"></a> JavaScript</li>
</ul>

  

