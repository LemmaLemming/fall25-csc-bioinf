# 

[Creating .sh file to run repo clone](#creating-.sh-file-to-run-repo-clone)

[Script: process\_data.sh](#script:-process_data.sh)

[How to Use](#how-to-use)

[Prompted Google Gemini 2.5 Pro Deep Research Module](#prompted-google-gemini-2.5-pro-deep-research-module)

[A Practical Guide to High-Performance Python with Codon v0.19](#heading=)

[Converting to Codon](#converting-to-codon)

[From Python to Codon: A Developer's Guide](#from-python-to-codon:-a-developer's-guide)

[Key Syntactic and Semantic Differences](#key-syntactic-and-semantic-differences)

[Interoperability with Python](#interoperability-with-python)

[Codon's Standard Library](#codon's-standard-library)

[Converted Codon Code](#converted-codon-code)

[dbg.codon](#dbg.codon)

[main.codon](#main.codon)

[How to Compile and Run](#how-to-compile-and-run)

[Creating Evaluate.sh](#creating-evaluate.sh)

# 

# Creating .sh file to run repo clone {#creating-.sh-file-to-run-repo-clone}

## cloned repo can be found in https://github.com/LemmaLemming/genome-assembly

create a sh file that does the following:

unzips data1, data2, data3, data4

call:

python main.py data1, then python main.py data2 soforth

for each python call, record the output into howards\_results/data1.txt, howards\_results/data2.txt and soforth

Of course. Here is a shell script that performs the requested tasks.

### **Script: process\_data.sh** {#script:-process_data.sh}

This script will unzip each data file, run your Python script on it, and save the output to a corresponding text file in the howards\_results directory.

Bash  
\#\!/bin/bash

\# This script automates the process of unzipping data files,  
\# running a Python script on them, and saving the results.

\# \--- Configuration \---  
\# List of data prefixes to process.  
\# Assumes your zip files are named data1.zip, data2.zip, etc.  
DATA\_SETS=("data1" "data2" "data3" "data4")

\# The name of your Python script.  
PYTHON\_SCRIPT="main.py"

\# The directory where results will be stored.  
RESULTS\_DIR="howards\_results"

\# \--- Script Start \---  
echo "Starting data processing..."

\# Create the results directory if it doesn't already exist.  
\# The '-p' flag prevents an error if the directory is already there.  
mkdir \-p "$RESULTS\_DIR"

\# Loop through each data set in the list.  
for data in "${DATA\_SETS\[@\]}"  
do  
  echo "--- Processing: $data \---"

  \# 1\. Unzip the data file.  
  \# The '-o' flag overwrites existing files without asking.  
  echo "Unzipping ${data}.zip..."  
  unzip \-o "${data}.zip"

  \# 2\. Call the Python script and redirect output.  
  \# The output of 'python main.py data1' will be saved to 'howards\_results/data1.txt'.  
  echo "Running Python script on $data..."  
  python "$PYTHON\_SCRIPT" "$data" \> "${RESULTS\_DIR}/${data}.txt"

  echo "Output saved to ${RESULTS\_DIR}/${data}.txt"  
done

echo "--- All processing complete\! ✅ \---"

---

### **How to Use** {#how-to-use}

1. **Save the File**: Save the code above into a file named process\_data.sh.  
2. **Make it Executable**: Open your terminal and run the following command to give the script permission to execute:  
3. Bash

chmod \+x process\_data.sh

4.   
5. **Run the Script**: Execute the script from your terminal by running:  
6. Bash

./process\_data.sh

7. 

The script will then create the howards\_results directory and populate it with data1.txt, data2.txt, and so on, each containing the output from your Python script.

# Prompted Google Gemini 2.5 Pro Deep Research Module {#prompted-google-gemini-2.5-pro-deep-research-module}

## Due diligence collected on codon. Partially for LLM memory as well. 

codon is a A high-performance, zero-overhead, extensible Python compiler with built-in NumPy support. The current version of codon is 19.3

write a report documenting the differences between codon and python. this report is informative as in anyone with python knowledge will be able to understand 19.3 codon syntax, import libraries from python into codon, import supported codon libraries by the end.

This is the current plan. What changes do you want to make?

(1) Access the official documentation and resources for Codon version 19.3 to establish a foundational understanding of its purpose, core features, and its positioning as a high-performance Python compiler. (2) Analyze the fundamental architectural differences between Codon and standard CPython. Detail how Codon's ahead-of-time (AOT) compilation, static typing, and zero-overhead approach contribute to performance gains over Python's interpreted, dynamic nature. (3) Create a comprehensive list of syntactic and semantic differences between Python and Codon. Focus on key areas such as type declarations, function definitions, new keywords, and any Python features that are modified or unsupported in Codon. (4) Investigate and explain the mechanism for interoperability between Codon and the Python ecosystem. Document the process, syntax, and any potential limitations when importing and using existing Python libraries within a Codon project. (5) Identify and describe the native libraries and modules provided by the Codon standard library. Pay special attention to its built-in, optimized support for NumPy and other libraries designed for high-performance computing. (6) Find side-by-side code examples that solve the same problem in both Python and Codon. Use these examples to practically illustrate the differences in syntax, performance, and overall programming paradigm. (7) Evaluate the ideal use cases for Codon, such as scientific computing, bioinformatics, and financial modeling, where performance is critical. Contrast this with scenarios where standard Python's flexibility might be more advantageous. (8) Synthesize all the gathered information into a structured report. The report should be organized to guide a Python developer through understanding Codon's syntax, its library ecosystem, and how to leverage Python libraries, fulfilling the user's request for an informative document.

No changes

# **A Practical Guide to High-Performance Python with Codon v0.19**

## **Introduction**

This guide serves as a practical introduction for Python developers transitioning to Codon, a high-performance, ahead-of-time (AOT) compiler. The user query specified "Codon 19.3," but it is important to clarify that the current major release series is v0.19. This report will focus on the features and updates pertinent to this version, which includes a significantly improved type-checking engine and backend upgrades to LLVM 20\.1  
Codon is frequently presented as a tool to make Python code faster, with benchmarks showing speedups of 10-100x or more over CPython on a single thread.2 However, to use it effectively, developers must understand a fundamental distinction: Codon is not merely a "faster Python." It is a distinct, statically-typed language that adopts Python's syntax to provide a familiar development experience.5 It is explicitly  
*not* a drop-in replacement for the CPython interpreter.2 This core difference—trading Python's runtime dynamism for compile-time performance—informs every aspect of its design and usage. The ultimate goal of Codon is to grant developers the ability to achieve performance on par with low-level languages like C/C++ without abandoning the accessible and productive syntax of Python.8

## **Section 1: The Codon Paradigm: Shifting from a Dynamic to a Static Mindset**

The primary challenge for a Python developer adopting Codon is not learning new syntax, but rather adjusting to a new programming paradigm. It requires unlearning the reliance on Python's dynamic nature and embracing the constraints and benefits of a static, compiled environment.

### **From Dynamic Interpretation to Ahead-of-Time (AOT) Compilation**

Unlike CPython, which interprets code line-by-line, Codon follows a traditional compilation workflow. Pythonic source code is first parsed into an Abstract Syntax Tree (AST). This AST then undergoes a rigorous static type-checking phase, where the type of every variable must be determined. Once validated, the code is converted into Codon's unique Intermediate Representation (CIR), then to LLVM IR, and finally compiled into native machine code.5 This process completely bypasses the Python interpreter, eliminating its associated overhead and, most notably, the Global Interpreter Lock (GIL), which enables true multithreading.2  
The consequence of this static, AOT compilation is that many of Python's hallmark dynamic features are disallowed. Because all types must be resolved at compile time, runtime "monkey patching" (modifying classes or modules on the fly) is not supported. Similarly, creating collections with heterogeneous types, such as a list containing both an integer and a string (\[1, 'a string'\]), is forbidden because the compiler must establish a single, uniform type for the collection's elements.10 These restrictions are the necessary trade-offs for generating highly optimized native code. The new type-checking engine introduced in Codon v0.19 significantly eases this transition by improving Python compatibility. It can now automatically infer class fields, removing the need for explicit declarations, and resolves function and class names in an order that more closely matches Python's runtime behavior.1  
This design philosophy reveals that Codon's innovation lies in its developer experience. It uses Python's familiar syntax as a façade for a powerful, statically-compiled language core. The learning curve is therefore not in the syntax itself, but in shifting from debugging runtime errors to resolving compile-time type errors. The choices of what to omit (e.g., runtime reflection) and what to build natively (e.g., a high-performance NumPy library) are deliberate, reflecting a strong focus on the scientific and high-performance computing (HPC) domains, where raw computational speed is paramount and dynamic features are often secondary.4

### **Core Data Type Divergences**

The most immediate and critical differences between Python and Codon are found in the behavior of fundamental data types.

* **Integers**: A standard Python int can be arbitrarily large, with the interpreter managing memory to accommodate any value. In contrast, Codon's int is a fixed-size, 64-bit signed integer, equivalent to int64\_t in C.10 This means it is subject to integer overflow. For example, adding 1 to the maximum 64-bit integer value will cause it to wrap around to a large negative number, a behavior that will be unexpected and potentially bug-inducing for developers accustomed to Python 3's safety.7 For cases requiring larger, fixed-size integers, Codon provides the  
  Int\[N\] type, where N is the bit width.10  
* **Strings**: Codon currently uses 8-bit ASCII strings, not the comprehensive Unicode strings used by Python.10 This has major implications for any application that handles international characters, emojis, or other non-ASCII text. Unicode support is planned for a future release, but for now, this is a significant compatibility limitation.  
* **Dictionaries**: Since Python 3.6, standard dictionaries preserve the insertion order of their keys. Codon's dict type makes no such guarantee, behaving like older versions of Python dictionaries where order is arbitrary.10 Any algorithm that implicitly or explicitly relies on key order will fail or produce incorrect results.  
* **Tuples**: In Codon, tuples are compiled down to static struct data structures. A direct consequence is that their length must be known at compile time.10 This prevents dynamic operations like converting a list of an unknown or variable size into a tuple at runtime.

### **Understanding Numeric Semantics (C vs. Python)**

By default, Codon prioritizes performance by adopting C-style numeric semantics. This means certain operations that would raise an exception in Python may proceed silently in Codon. For example, division by zero might not raise a ZeroDivisionError, and functions in the math module may not perform domain checks (e.g., for the square root of a negative number).10  
For developers who require Python's safer, more predictable numeric behavior, Codon provides a crucial compiler flag: \-numerics=py. Using this flag enforces Python's semantics, such as raising ZeroDivisionError and performing domain checks, at the cost of a minor performance penalty.1 This is a project-level decision that balances raw speed against runtime safety.

| Feature | CPython 3 Behavior | Codon Behavior | Key Implication for Developers |
| :---- | :---- | :---- | :---- |
| **Integer (int)** | Arbitrary precision; never overflows. | 64-bit signed integer; subject to overflow (wraps around). | Code handling very large numbers must be rewritten, possibly using Int\[N\] or a different algorithm. |
| **String (str)** | Unicode (UTF-8 by default). | ASCII (8-bit). | Not suitable for international text or non-ASCII characters without manual encoding/decoding. |
| **Dictionary (dict)** | Preserves key insertion order (since 3.6). | Does not preserve insertion order. | Algorithms relying on ordered keys will fail and must be adapted. |
| **Tuple (tuple)** | Can be created dynamically from any iterable. | Length must be known at compile time. | Cannot convert an arbitrarily-sized list to a tuple at runtime. |
| **List/Collection Content** | Can contain objects of different types (e.g., \[1, "a"\]). | Must contain objects of a single, uniform type. | Requires more careful data structuring; union types can provide some flexibility.1 |

## **Section 2: The Codon Toolchain: Compilation and Execution**

Effectively using Codon requires familiarity with its command-line interface (CLI), which is the primary tool for compiling and running code.

### **Installation and Environment Setup**

Codon can be installed on Linux and macOS systems with a single command, which downloads and runs an installation script 3:

Bash

/bin/bash \-c "$(curl \-fsSL https://exaloop.io/install.sh)"

The installation process requires a C++ compiler (like GCC or Clang) to be present on the system for linking the final executables.15 After installation, the  
codon command becomes available. Its version can be verified with codon \--version.

### **Mastering the codon Command**

The codon CLI has two primary modes of operation for executing code:

* codon run: This command compiles and immediately executes a script. It is convenient for development and rapid testing. However, the reported execution time will include the compilation overhead, which can be misleading when trying to measure the true performance of the compiled code.3  
* codon build: This is the standard command for producing a standalone, native executable. It separates the compilation step from execution, making it the correct choice for creating production artifacts and conducting accurate performance benchmarks.3

### **The Critical \-release Flag**

For any task where performance is a concern, the \-release flag is essential. This flag enables a full suite of LLVM optimizations, resulting in significantly faster code. The performance difference between a default (debug) build and a release build can be substantial.3  
More than just a simple optimization switch, the \-release flag acts as a fundamental "mode switch" for the compiler. For instance, when compiling code that uses NumPy, a standard build might link against a compatibility layer for the CPython NumPy library. In contrast, a build with \-release will link against Codon's fully native, highly optimized NumPy implementation. This can result in a smaller, much faster binary, demonstrating that the flag influences not just LLVM's optimization passes but also the Codon frontend's library selection and code generation strategies.16

### **Generating Different Artifacts**

The codon build command is versatile and can produce several types of output:

* **Executable**: The default output is a standalone executable. The output filename can be specified with the \-o flag: codon build \-release my\_script.py \-o my\_app.3  
* **Python Extension Module**: A key feature for incremental adoption is the ability to compile Codon code into a shared library (.so or .dylib) that can be imported directly into a standard Python program. This is achieved with the \-pyext flag. It is often necessary to also use \--relocation-model=pic to generate position-independent code required for shared libraries.14  
* **LLVM IR**: For advanced users interested in compiler internals, codon build \-llvm will output the human-readable LLVM Intermediate Representation. This can be used to inspect how Codon translates high-level code and to verify that certain optimizations are being applied.3

| Flag/Command | Purpose | Example Usage |
| :---- | :---- | :---- |
| codon run | Compiles and immediately executes a script. Best for development. | codon run my\_script.py |
| codon build | Compiles a script into a standalone artifact (e.g., executable). | codon build my\_script.py |
| \-release | Enables all performance optimizations. Essential for production/benchmarking. | codon build \-release my\_script.py |
| \-o \<file\> | Specifies the output file name for the build artifact. | codon build \-release my\_script.py \-o my\_app |
| \-pyext | Compiles the code into a Python extension module. | codon build \-release \-pyext \--relocation-model=pic my\_module.py |
| \-numerics=py | Enforces Python's numeric semantics (e.g., ZeroDivisionError). | codon run \-numerics=py safe\_math.py |
| \-linker-flags | Passes additional flags to the system linker during the build process. | codon build \-linker-flags '-Wl,-rpath,/opt/lib' program.py |

## **Section 3: High-Performance Libraries: The Codon Native Ecosystem**

Codon's performance advantage extends beyond the core language to its libraries. By re-implementing key Python libraries natively, Codon ensures they can be fully analyzed and optimized by the compiler, a level of integration impossible in CPython.

### **Navigating the Codon Standard Library**

Codon provides native implementations for a large portion of Python's standard library, including modules like math, sys, os, collections, and datetime.18 While the goal is API compatibility, there are important implementation-specific details:

* **Reproducibility**: The random module is designed to match CPython's output for a given seed, which is critical for reproducible simulations and testing.18  
* **Performance**: The re module uses Google's high-performance RE2 library as its backend, offering faster regular expression matching.18  
* **Incompatibility**: The pickle module uses a custom serialization format. This means objects pickled with Codon cannot be unpickled by CPython, and vice-versa. This is a significant interoperability constraint that developers must be aware of when designing systems that mix Codon and Python components.18

In addition to Python-compatible modules, Codon introduces several of its own, such as openmp and gpu, which provide direct access to its advanced parallelism features.18

### **Deep Dive: The Codon-Native NumPy Library**

For many scientific and data-intensive applications, NumPy is the most critical library. Codon includes a feature-complete, native re-implementation of the NumPy API.19 This is not a simple wrapper around the original C library; it is a new implementation written in Codon itself, designed from the ground up to be "compiler-aware".21  
The API is identical to standard NumPy, allowing developers to use familiar syntax like import numpy as np and functions like np.arange and np.array.19 The performance gains come from the deep integration between this library and the Codon compiler. Unlike in CPython, where a NumPy operation is an opaque call to a pre-compiled C function, the Codon compiler can "see inside" its native NumPy calls. This enables powerful, cross-procedural optimizations.  
A prime example of this is **operator fusion**. Consider the expression y \= a \* x \+ b, where a, x, and b are large arrays. Standard NumPy would execute this in two passes: first, it would create a temporary array to hold the result of a \* x, and then it would perform the addition with b. Codon's compiler can analyze the entire expression and fuse the operations into a single loop that iterates over the arrays, performing the multiplication and addition for each element in one pass. This completely eliminates the memory allocation and overhead of the temporary array, resulting in significant speedups.19  
This level of optimization is possible because of Codon-NumPy's static ndarray\[dtype, ndim\] type. By making the array's data type and, crucially, its number of dimensions part of the static type system, the compiler has perfect information at compile time. This allows it to generate highly specialized and optimized machine code for array operations, a feat that is impossible in Python's dynamic, library-centric model.10

## **Section 4: Bridging Worlds: Interoperability with the Python Ecosystem**

While Codon's native ecosystem is powerful, the vastness of the Python ecosystem means developers will inevitably need to use libraries that have not been ported. Codon provides a robust interoperability bridge to call any Python library, but using it effectively requires understanding its performance implications.

### **Setting Up the Bridge: The CODON\_PYTHON Environment Variable**

To enable Python interoperability, Codon must be able to locate the CPython shared library (e.g., libpython3.11.so or libpython3.11.dylib). This is done by setting the CODON\_PYTHON environment variable to the absolute path of this file. This is a common point of initial friction, and failure to set it correctly will result in errors when trying to import Python modules.3 When working within a Python virtual environment, the  
PYTHON\_PATH environment variable should also be set to the site-packages directory of that environment to ensure Codon can find installed packages.22

### **The from python import Statement**

The primary mechanism for using external libraries is the from python import \<module\> statement. This allows a Codon program to import any installed Python package, such as matplotlib or pandas.3  
It is critical to understand what happens when this feature is used. The imported Python code is not compiled by Codon. Instead, it is executed by an embedded CPython interpreter, making calls through CPython's C API.22 This means the code runs at standard Python speeds, is subject to the GIL, and does not benefit from any of Codon's optimizations.11 Therefore, this feature should be used for functionality, not for performance-critical computations.

### **The @python Decorator: Creating Interpreter Enclaves**

For situations where only a small piece of logic requires Python's dynamic features, Codon provides the @python decorator. A function marked with this decorator will be executed entirely by the Python interpreter, even though it is defined within a Codon source file.6 This is useful for isolating small, incompatible code snippets without needing to manage separate files.

### **Managing the Performance Toll: Data Conversion**

The boundary between the Codon-compiled world and the Python-interpreted world should be thought of as a "performance firewall." Every time data crosses this boundary, a conversion must take place. Codon uses internal \_\_to\_py\_\_ and \_\_from\_py\_\_ magic methods to convert data structures between their native Codon representation and Python's PyObject format.22  
This conversion process has a non-zero overhead. While negligible for single, infrequent calls with small amounts of data, it can become a major performance bottleneck if large data structures (like arrays) are passed back and forth between Codon and Python inside a tight loop. The most performant applications are designed to minimize traffic across this firewall. A common and effective pattern is to use Python libraries at the very beginning of a program (e.g., to load data) and at the very end (e.g., to plot results with matplotlib), while ensuring that all intensive computation and looping occurs exclusively within the native Codon environment. The development of a native Codon-NumPy was motivated precisely because using CPython's NumPy via this bridge "leaves a lot of performance on the table".21

| Strategy | Primary Use Case | Performance Impact | Example |
| :---- | :---- | :---- | :---- |
| **Native Codon Code** | Performance-critical computations, loops, algorithms. | Highest performance; fully compiled and optimized. | def fib(n): return n if n \< 2 else fib(n-1) \+ fib(n-2) |
| **from python import** | Using non-performance-critical Python libraries for I/O, plotting, etc. | High overhead; code runs in CPython interpreter, subject to GIL. | from python import matplotlib.pyplot as plt |
| **@python decorator** | Isolating small, dynamic functions that cannot be expressed in Codon. | High overhead (same as from python import) for the decorated function. | @python def dynamic\_func():... |
| **@codon.jit decorator** | Incrementally accelerating a single slow function within an existing Python codebase. | High performance for the JIT-compiled function; some overhead on the first call. | @codon.jit def hotspot\_function(arr):... |

## **Section 5: Unleashing True Parallelism: Multithreading and GPU Programming**

Perhaps the most significant advantage Codon offers over CPython is its ability to break free from the Global Interpreter Lock and unlock true hardware parallelism. This is achieved through a set of intuitive, high-level language features that act as interfaces to powerful, low-level parallel programming APIs.

### **Breaking the GIL: Native Multithreading with @par**

The @par decorator is the primary tool for parallelizing for loops in Codon.3 By simply adding this decorator before a loop, a developer instructs the compiler to distribute the loop's iterations across multiple CPU cores. This is a Pythonic, high-level syntax for the well-established OpenMP API.3  
For example, a sequential prime number calculation in Python can be parallelized in Codon with a single line of code 24:  
**Python (Sequential):**

Python

total \= 0  
for i in range(2, limit):  
    if is\_prime(i):  
        total \+= 1

**Codon (Parallel):**

Python

total \= 0  
@par(num\_threads=16)  
for i in range(2, limit):  
    if is\_prime(i):  
        total \+= 1

The @par decorator supports several parameters that map directly to OpenMP concepts, allowing for fine-grained control:

* num\_threads: Specifies the exact number of threads to use.3  
* schedule: Controls how iterations are assigned to threads (e.g., dynamic for uneven workloads).3  
* collapse: Allows the compiler to parallelize the entire iteration space of nested loops.1

Crucially, Codon's compiler is intelligent enough to handle common parallel programming pitfalls automatically. For instance, in the example above, the total \+= 1 statement is a reduction. The compiler automatically transforms this into an atomic operation to prevent race conditions where multiple threads might try to update the variable simultaneously.3

### **A Primer on GPU Acceleration**

For massively parallel workloads, Codon provides access to GPU programming through the @gpu.kernel decorator. This feature provides a high-level abstraction over the CUDA programming model, allowing developers to write GPU kernels in Pythonic syntax.3 A function decorated with  
@gpu.kernel is compiled to run on the GPU, and variables like gpu.block.x and gpu.thread.x provide access to the GPU's execution hierarchy, similar to CUDA.21 This dramatically lowers the barrier to entry for GPU computing, enabling Python developers to leverage this hardware without needing to write low-level C++ or CUDA C code.

## **Conclusion: A Strategic Approach to Adopting Codon**

Codon offers a compelling path to high performance for Python developers, but its adoption requires a strategic approach centered on understanding its core trade-off: sacrificing Python's runtime dynamism for C/C++-level compiled performance.

### **Identifying Ideal Use Cases**

Codon excels in domains where applications are CPU-bound and dominated by numerical computation. Ideal use cases include:

* **Strengths**: Scientific computing, bioinformatics, quantitative finance, machine learning model inference, image and signal processing, and any algorithm involving intensive loops or large array manipulations.4  
* **Weaknesses**: Codon is less suited for I/O-bound applications like web servers or for scripts that rely heavily on Python's dynamic features, such as introspection, runtime code generation, or extensive monkey-patching. Projects requiring deep integration with large Python frameworks like Django may also face challenges, as calls across the CPython bridge can negate performance gains.8

### **Incremental Adoption Pathways**

For developers looking to integrate Codon into existing projects, several pathways are available, each offering a different balance of effort and performance gain:

1. **The JIT Decorator (@codon.jit)**: This is the lowest-friction entry point. By installing the codon-jit package from pip, a developer can apply the @codon.jit decorator to a single, performance-critical function within a larger Python application. Codon will just-in-time compile this specific function at runtime, providing a significant speed boost for that hotspot with minimal code changes. This approach is analogous to using Numba and is ideal for targeted optimization.6  
2. **Python Extensions (-pyext)**: This is the next step for more significant performance gains. A performance-sensitive module can be isolated into its own .py file and compiled into a native shared library using codon build \-pyext. This ahead-of-time compiled module can then be imported back into the main Python application like any other C extension. This method provides the full benefit of AOT optimization for a substantial part of the codebase while leaving the rest of the application in standard Python.14  
3. **Full Application Rewrite**: For new projects or applications where performance is the primary requirement, a full rewrite in Codon is the most powerful option. This approach leverages the full extent of Codon's capabilities, including its static type system, native libraries, and advanced parallelism features, to achieve the best possible performance.

By choosing the appropriate adoption strategy, Python developers can strategically leverage Codon to overcome performance bottlenecks, unlock true hardware parallelism, and deliver C-level speed without leaving the familiarity of the Python ecosystem.

#### **Works cited**

1. Changelog | Codon, accessed September 20, 2025, [https://docs.exaloop.io/start/changelog/](https://docs.exaloop.io/start/changelog/)  
2. Codon: Documentation, accessed September 20, 2025, [https://docs.exaloop.io/](https://docs.exaloop.io/)  
3. exaloop/codon: A high-performance, zero-overhead, extensible Python compiler with built-in NumPy support \- GitHub, accessed September 20, 2025, [https://github.com/exaloop/codon](https://github.com/exaloop/codon)  
4. 'Codon' Compiles Python to Native Machine Code That's Even Faster Than C \- Slashdot, accessed September 20, 2025, [https://developers.slashdot.org/story/23/03/19/0156208/codon-compiles-python-to-native-machine-code-thats-even-faster-than-c](https://developers.slashdot.org/story/23/03/19/0156208/codon-compiles-python-to-native-machine-code-thats-even-faster-than-c)  
5. Codon: A Compiler for High-Performance Pythonic Applications and DSLs \- MIT, accessed September 20, 2025, [https://cap.csail.mit.edu/sites/default/files/research-pdfs/Codon-%20A%20Compiler%20for%20High-Performance%20Pythonic%20Applications%20and%20DSLs.pdf](https://cap.csail.mit.edu/sites/default/files/research-pdfs/Codon-%20A%20Compiler%20for%20High-Performance%20Pythonic%20Applications%20and%20DSLs.pdf)  
6. How do you think about Codon? \- Offtopic \- Julia Programming Language, accessed September 20, 2025, [https://discourse.julialang.org/t/how-do-you-think-about-codon/119842](https://discourse.julialang.org/t/how-do-you-think-about-codon/119842)  
7. Make your Python scripts upto 100x faster by compiling them using Codon \- YouTube, accessed September 20, 2025, [https://www.youtube.com/watch?v=AA9Lj1HivD0](https://www.youtube.com/watch?v=AA9Lj1HivD0)  
8. Codor Python Compiler Promises to Achieve C/C++ Performance And Speeds, accessed September 20, 2025, [https://community.element14.com/technologies/code\_exchange/b/blog/posts/codor-python-compiler-promises-to-achieve-c-c-performance-and-speeds](https://community.element14.com/technologies/code_exchange/b/blog/posts/codor-python-compiler-promises-to-achieve-c-c-performance-and-speeds)  
9. Codon: A High-Performance Python Compiler with 100x Speedup and Native Multithreading, accessed September 20, 2025, [https://medium.com/top-python-libraries/codon-a-high-performance-python-compiler-with-100x-speedup-and-native-multithreading-3c650d90eb62](https://medium.com/top-python-libraries/codon-a-high-performance-python-compiler-with-100x-speedup-and-native-multithreading-3c650d90eb62)  
10. Overview | Codon, accessed September 20, 2025, [https://docs.exaloop.io/language/overview/](https://docs.exaloop.io/language/overview/)  
11. Codon: A high-performance Python-like compiler using LLVM | Hacker News, accessed September 20, 2025, [https://news.ycombinator.com/item?id=33908576](https://news.ycombinator.com/item?id=33908576)  
12. Releases · exaloop/codon \- GitHub, accessed September 20, 2025, [https://github.com/exaloop/codon/releases](https://github.com/exaloop/codon/releases)  
13. Codon: Python now superior performance to C++ . Is Python now undisputed \> than C++ : r/Python \- Reddit, accessed September 20, 2025, [https://www.reddit.com/r/Python/comments/11t4p8p/codon\_python\_now\_superior\_performance\_to\_c\_is/](https://www.reddit.com/r/Python/comments/11t4p8p/codon_python_now_superior_performance_to_c_is/)  
14. Usage | Codon \- Exaloop, accessed September 20, 2025, [https://docs.exaloop.io/start/usage/](https://docs.exaloop.io/start/usage/)  
15. Introduction to Codon, the Python Compiler \- Makiki, accessed September 20, 2025, [http://www.makikiweb.com/Pi/intro\_to\_codon.html](http://www.makikiweb.com/Pi/intro_to_codon.html)  
16. Codon: Python Compiler Update \- USENIX, accessed September 20, 2025, [https://www.usenix.org/publications/loginonline/codon-python-compiler-update](https://www.usenix.org/publications/loginonline/codon-python-compiler-update)  
17. Python-based compiler achieves orders-of-magnitude speedups | MIT News, accessed September 20, 2025, [https://news.mit.edu/2023/codon-python-based-compiler-achieve-orders-magnitude-speedups-0314](https://news.mit.edu/2023/codon-python-based-compiler-achieve-orders-magnitude-speedups-0314)  
18. Standard Library | Codon, accessed September 20, 2025, [https://docs.exaloop.io/libraries/stdlib/](https://docs.exaloop.io/libraries/stdlib/)  
19. NumPy | Codon, accessed September 20, 2025, [https://docs.exaloop.io/libraries/numpy/](https://docs.exaloop.io/libraries/numpy/)  
20. raw.githubusercontent.com, accessed September 20, 2025, [https://raw.githubusercontent.com/exaloop/codon/develop/README.md](https://raw.githubusercontent.com/exaloop/codon/develop/README.md)  
21. Codon in 2025: New compiler-optimized NumPy implementation. Switching to an open source license. | Exaloop, accessed September 20, 2025, [https://www.exaloop.io/blog/codon-2025](https://www.exaloop.io/blog/codon-2025)  
22. Call Python from Codon | Codon, accessed September 20, 2025, [https://docs.exaloop.io/integrations/python/python-from-codon/](https://docs.exaloop.io/integrations/python/python-from-codon/)  
23. Can codon be used on programs that use NumPy and Pandas? \#228 \- GitHub, accessed September 20, 2025, [https://github.com/exaloop/codon/discussions/228](https://github.com/exaloop/codon/discussions/228)  
24. Real Multithreading in Python with Codon | by Rahul Beniwal ..., accessed September 20, 2025, [https://python.plainenglish.io/real-multithreading-in-python-with-codon-9eb2c6c2faac](https://python.plainenglish.io/real-multithreading-in-python-with-codon-9eb2c6c2faac)  
25. How to use Codon, a new alternative to Python \- YouTube, accessed September 20, 2025, [https://www.youtube.com/watch?v=ozPVLPRnYb8](https://www.youtube.com/watch?v=ozPVLPRnYb8)

# Converting to Codon {#converting-to-codon}

Please take a look at my [main.py](http://main.py), [utils.py](http://utils.py) and [dbg.py](http://dbg.py) files.   
I’ve already installed codon and the seq plugin. 

Of course\! Here is your report on the differences between Python and Codon to get you started on your project.

### **From Python to Codon: A Developer's Guide** {#from-python-to-codon:-a-developer's-guide}

This report provides a practical guide for Python developers looking to leverage the power of Codon, a high-performance, ahead-of-time compiler that supercharges Python code. We'll cover the key differences in syntax, how to work with Python libraries, and how to use Codon's own set of powerful, built-in libraries.

---

### **Key Syntactic and Semantic Differences** {#key-syntactic-and-semantic-differences}

While Codon is designed to be a seamless extension of Python, there are a few key differences to keep in mind, primarily centered around Codon's static type system.

* **Static Typing**: Unlike Python's dynamic typing, Codon is **statically typed**. This means you must declare the types of all variables and function arguments. This is the biggest change from Python, but it's also the source of Codon's performance gains.  
  * **Python:**  
  * Python

def add(a, b):  
    return a \+ b

*   
  * **Codon:**  
  * Python

def add(a: int, b: int) \-\> int:  
    return a \+ b

*   
* **Data Types**: Codon has a rich set of built-in data types that are compatible with Python's, but with a few additions. For example, Codon has explicit integer types of different sizes (e.g., i8, i16, i32, i64) and unsigned integers (e.g., u8, u16, u32, u64).  
* **No Runtime Type-Checking**: In Codon, type-checking is done at compile time. This means that you can't use Python's isinstance or type functions to check the type of a variable at runtime.  
* **Modules**: Codon has its own module system that is similar to Python's, but with a few differences. For example, Codon does not support dynamic module loading.

---

### **Interoperability with Python** {#interoperability-with-python}

One of Codon's most powerful features is its seamless interoperability with Python. You can import and use any Python library in your Codon code with zero overhead.

* **Importing Python Libraries**: To import a Python library, you use the from python import syntax. For example, to import the numpy library, you would use:  
* Python

from python import numpy as np

*   
* **Calling Python Functions**: Once you've imported a Python library, you can call its functions just as you would in Python.  
* **The @python Decorator**: For functions that need to interact heavily with Python objects or libraries, you can use the @python decorator. This tells the Codon compiler to treat the function as a regular Python function, allowing you to use Python's dynamic features within it.

---

### **Codon's Standard Library** {#codon's-standard-library}

Codon comes with a rich standard library that includes many of the same modules as Python's standard library, but with optimized, compiled implementations. It also includes Codon-specific modules for performance-critical tasks.

* **Built-in Modules**: Codon's standard library includes modules for common tasks like working with strings, files, and data structures. It also has a powerful re module for regular expressions that is fully compatible with Python's.  
* **Native NumPy Library**: Codon has a built-in, native implementation of the NumPy library. This library provides the same API as the Python version of NumPy, but with performance that is often an order of magnitude faster. It also supports multithreading and GPU execution.  
* **Bioinformatics with the seq Plugin**: For bioinformatics tasks, Codon has a seq plugin that provides a bio module. This module contains tools for working with biological sequences, including functions for reverse complementation, k-merization, and sequence alignment.

---

### **Converted Codon Code** {#converted-codon-code}

Here is the converted, Codon-compatible code for your genome assembly project.

**utils.codon**

Python  
import os  
from typing import List, Tuple

def read\_fasta(path: str, name: str) \-\> List\[str\]:  
    data: List\[str\] \= \[\]  
    with open(os.path.join(path, name), 'r') as f:  
        for line in f.readlines():  
            line \= line.strip()  
            if line and line\[0\] \!= '\>':  
                data.append(line)  
    print(name, len(data), len(data\[0\]))  
    return data

def read\_data(path: str) \-\> Tuple\[List\[str\], List\[str\], List\[str\]\]:  
    short1 \= read\_fasta(path, "short\_1.fasta")  
    short2 \= read\_fasta(path, "short\_2.fasta")  
    long1 \= read\_fasta(path, "long.fasta")  
    return short1, short2, long1

#### **dbg.codon** {#dbg.codon}

Python  
from typing import Dict, Set, List, Optional  
import copy

def reverse\_complement(key: str) \-\> str:  
    complement: Dict\[str, str\] \= {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}  
    return "".join(complement\[base\] for base in reversed(key))

class Node:  
    \_children: Set\[int\]  
    \_count: int  
    kmer: str  
    visited: bool  
    depth: int  
    max\_depth\_child: Optional\[int\]

    def \_\_init\_\_(self, kmer: str):  
        self.\_children \= set()  
        self.\_count \= 0  
        self.kmer \= kmer  
        self.visited \= False  
        self.depth \= 0  
        self.max\_depth\_child \= None

    def add\_child(self, kmer\_idx: int):  
        self.\_children.add(kmer\_idx)

    def increase(self):  
        self.\_count \+= 1

    def reset(self):  
        self.visited \= False  
        self.depth \= 0  
        self.max\_depth\_child \= None

    def get\_count(self) \-\> int:  
        return self.\_count

    def get\_children(self) \-\> List\[int\]:  
        return list(self.\_children)

    def remove\_children(self, target: Set\[int\]):  
        self.\_children \= self.\_children \- target

class DBG:  
    k: int  
    nodes: Dict\[int, Node\]  
    kmer2idx: Dict\[str, int\]  
    kmer\_count: int

    def \_\_init\_\_(self, k: int, data\_list: List\[List\[str\]\]):  
        self.k \= k  
        self.nodes \= {}  
        self.kmer2idx \= {}  
        self.kmer\_count \= 0  
        self.\_check(data\_list)  
        self.\_build(data\_list)

    def \_check(self, data\_list: List\[List\[str\]\]):  
        assert len(data\_list) \> 0  
        assert self.k \<= len(data\_list\[0\]\[0\])

    def \_build(self, data\_list: List\[List\[str\]\]):  
        for data in data\_list:  
            for original in data:  
                rc \= reverse\_complement(original)  
                for i in range(len(original) \- self.k):  
                    self.\_add\_arc(original\[i: i \+ self.k\], original\[i \+ 1: i \+ 1 \+ self.k\])  
                    self.\_add\_arc(rc\[i: i \+ self.k\], rc\[i \+ 1: i \+ 1 \+ self.k\])

    def \_add\_node(self, kmer: str) \-\> int:  
        if kmer not in self.kmer2idx:  
            self.kmer2idx\[kmer\] \= self.kmer\_count  
            self.nodes\[self.kmer\_count\] \= Node(kmer)  
            self.kmer\_count \+= 1  
        idx \= self.kmer2idx\[kmer\]  
        self.nodes\[idx\].increase()  
        return idx

    def \_add\_arc(self, kmer1: str, kmer2: str):  
        idx1 \= self.\_add\_node(kmer1)  
        idx2 \= self.\_add\_node(kmer2)  
        self.nodes\[idx1\].add\_child(idx2)

    def \_get\_count(self, child\_idx: int) \-\> int:  
        return self.nodes\[child\_idx\].get\_count()

    def \_get\_sorted\_children(self, idx: int) \-\> List\[int\]:  
        children \= self.nodes\[idx\].get\_children()  
        children.sort(key=self.\_get\_count, reverse=True)  
        return children

    def \_get\_depth(self, idx: int) \-\> int:  
        if not self.nodes\[idx\].visited:  
            self.nodes\[idx\].visited \= True  
            children \= self.\_get\_sorted\_children(idx)  
            max\_depth, max\_child \= 0, None  
            for child in children:  
                depth \= self.\_get\_depth(child)  
                if depth \> max\_depth:  
                    max\_depth, max\_child \= depth, child  
            self.nodes\[idx\].depth, self.nodes\[idx\].max\_depth\_child \= max\_depth \+ 1, max\_child  
        return self.nodes\[idx\].depth

    def \_reset(self):  
        for idx in self.nodes:  
            self.nodes\[idx\].reset()

    def \_get\_longest\_path(self) \-\> List\[int\]:  
        max\_depth, max\_idx \= 0, None  
        for idx in self.nodes:  
            depth \= self.\_get\_depth(idx)  
            if depth \> max\_depth:  
                max\_depth, max\_idx \= depth, idx

        path: List\[int\] \= \[\]  
        curr \= max\_idx  
        while curr is not None:  
            path.append(curr)  
            curr \= self.nodes\[curr\].max\_depth\_child  
        return path

    def \_delete\_path(self, path: List\[int\]):  
        path\_set \= set(path)  
        for idx in path:  
            if idx in self.nodes:  
                del self.nodes\[idx\]  
        for idx in self.nodes:  
            self.nodes\[idx\].remove\_children(path\_set)

    def \_concat\_path(self, path: List\[int\]) \-\> Optional\[str\]:  
        if not path:  
            return None  
        concat \= self.nodes\[path\[0\]\].kmer  
        for i in range(1, len(path)):  
            concat \+= self.nodes\[path\[i\]\].kmer\[-1\]  
        return concat

    def get\_longest\_contig(self) \-\> Optional\[str\]:  
        self.\_reset()  
        path \= self.\_get\_longest\_path()  
        contig \= self.\_concat\_path(path)  
        self.\_delete\_path(path)  
        return contig

#### **main.codon** {#main.codon}

Python  
from dbg import DBG  
from utils import read\_data  
import sys  
import os  
from typing import List

def main():  
    if len(sys.argv) \< 2:  
        print("Usage: codon run \-plugin seq main.codon \<data\_directory\>")  
        return

    data\_dir \= sys.argv\[1\]  
    short1, short2, long1 \= read\_data(data\_dir)

    k \= 25  
    dbg \= DBG(k=k, data\_list=\[short1, short2, long1\])  
      
    output\_file \= os.path.join(data\_dir, 'contig.fasta')  
    with open(output\_file, 'w') as f:  
        for i in range(20):  
            c \= dbg.get\_longest\_contig()  
            if c is None:  
                break  
            print(i, len(c))  
            f.write(f'\>contig\_{i}\\n')  
            f.write(c \+ '\\n')

if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

### **How to Compile and Run** {#how-to-compile-and-run}

To compile and run your Codon project, use the following command:

Bash  
\~/.codon/bin/codon run \-plugin seq main.codon \<path\_to\_data\_directory\>

Replace \<path\_to\_data\_directory\> with the path to the directory containing your FASTA files. This command will compile and run your main.codon program, using the seq plugin for any bioinformatics-specific functions.

I hope this report helps you on your journey with Codon\! Let me know if you have any other questions.

# Creating [Evaluate.sh](http://Evaluate.sh)  {#creating-evaluate.sh}

## Output .sh file from pseudocode  

