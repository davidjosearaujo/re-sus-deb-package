<!--
 Copyright 2024 David Araújo
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
     https://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->

---
geometry: margin=25mm
title: Reverse Engineering - Suspicious Deb package
author: Tiago Silvestre - 103554, David Araújo - 93444
date: May XX, 2024
---

# Table of Contents
1. [Executive Summary](#executive-summary)
2. [Major Findings](#major-findings)
3. [Indicators of Compromise](#indicators-of-compromise)
4. [Description of the files](#description-of-the-files)


# Execute summary

<!-- TODO -->

# Major Findings

For this project, we were given a DEB file with the name *ansible-core_2.14.3-1+ua_all.deb*, and it is also said that "name and version do not match the original package". Because of this we search the internet for the original packaged named *ansible-core_2.14.3-1_all.deb*.

