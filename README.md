# Lookup
A simple python command-line tool to fetch and display meaning, synonyms and antonyms of any word right in the terminal.

#### Usage: lookup [OPTION] [WORD] 

    List the synonym,antonym and meaning of a word in the terminal
    
    Options:
        -m                  Fetch meaning of a word
        -s                  Fetch synonyms of a word
        -a                  Fetch antonyms of a word
    
    Example:
        
        $ lookup -m scrupulous      (Fetches the meaning of Scrupulous)
        $ lookup -s scrupulous      (Fetches the synonyms of Scrupulous)
        $ lookup -a scrupulous      (Fetches the antonyms of Scrupulous)

#### Installation:

    Requirements:
        
        Make sure you have python3 and pip3 installed on your system.
        Rest of the dependencies will be installed automatically.
        Also if your local bin directory is not added the PATH by default, make sure to add it.
        
        To do that add the following line at the end of your ~/.profile or ~/.bash_profile:
        
            **export PATH=$PATH:~/.local/bin/**
            
        Save and exit then run:
            
            $ source .profile
                    or
            $ source .bash_profile
             

    From Github:
        
        1. Clone this repository
        2. navigate to the directory:
            
            $ cd lookup

           then:

            $ pip3 install .

        3. You are good to go!
      

