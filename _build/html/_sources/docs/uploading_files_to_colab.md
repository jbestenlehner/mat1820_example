### Uploading files hosted on Websites

The Colab cloud-service uses Linux. So Linux commands can be used to handle data. To upload data from Blackboard or website in general you can use the command `wget`. Linux commands within your code cell are executed with a "!" in front of the command.

```bash
!wget <link>
```

`<link>` is the place holder for a web link, for example:

```bash
!wget https://raw.githubusercontent.com/jbestenlehner/mat1820_example/refs/heads/main/data/somefile.txt #uploads the file to your Colab session
!ls               # lists files in your Colab session
!cat somefile.txt # shows the content of your file
```
Note: `ls`, `cat` or any other Linux command can be also used in the Terminal, when you open on the Terminal.
