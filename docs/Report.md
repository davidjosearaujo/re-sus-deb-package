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

![Directory Struture](./images/01_dir_struct_different.png)

Using `dpkg-deb` to expose the content of both DEB files, when doing so we can clearly see that the one infected has an additional directory. Inside the *lib* directory there is a descriptor for a system service.

![Ansibled service descriptor](./images/02_ansible_service.png)

The important bit of this descriptor is the binary file it executes, explicit at `ExecStart=/usr/lib/ansibled`.

![Ansibled binary file](./images/03_service_exec_binary.png)

We can make sure that this is indeed an additional file an we are comparing the right packages by using the `deephash` tool to compare the hash of multiple files. Doing this reveals equal hash ensuring that this are indeed the same packages and that file is extra.

![Hash comparison](./images/04_matching_hash_with_additional_binary_file.png)

## Ansibled File Analysis

![File type](./images/05_exiftool_architecture_type_ansibled.png)

We start by using `exiftool` to discover the type of the file tna the CPU architecture for which is is intended run in. We can easily see that it is an ELF file intended to run at an x86 64bit architecture.

We also search for clear text using the `strings` tools.

![Strings inside ansibled (1)](./images/06_01_strings_ansibled.png)
![Strings inside ansibled (2)](./images/06_strings_ansibled.png)

We discover that whatever this binary does it will at least involve **sockets** and that gives us a **clue to search for information such as addresses and port numbers**. Not only that, it also handles some sort of **file writing and reading**, as well as the **suspicious search for process IDs** and the apparent access to a file with a given PID in the _/proc_ directory.

Because this appears to be reading and writing, we can assume that there will ne *syscalls*, as so we run `strace` to discovery what is being accessed during execution.

![Strace of ansibled](./images/13_strace_ansibled.png)

The first thing we can see is the binary trying to access a file with an unusual name _qhu*dkvlgi'a+ijfn_ but this is not found. Later it will try to again access it as well as another file at the _tmp_ directory with the name _guide.pdf_.

These files are never found, meaning their do not yet exist? This appears to trigger the creation of a socket object.

![Socket and PDF download](./images/14_strace_ansibled_recv_pdf.png)

As we can see, the binary tem establishes a connection with the IP _192.168.160.143_, and with this IP it will proceed to make a GET request to the endpoint _/guide.pdf_. We can now assume that in the beginning the binary was checking for the existence of this file, and given that it did not exist, it will now try to download it.

What we then see (in the blocks in blue), is the response from the server with the contents for the _guide.pdf_ and the binary writing them to the file in _tmp_.

![Reading and transforming guide.pdf](./images/15_strace_ansibled_efem_file_PDF_to_ELF.png)

TODO