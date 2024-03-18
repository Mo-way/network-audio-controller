This program exists for my own personal use. I've published it here only so
that others who find it useful can give me feedback or examine what I've done
to more easily implement their own version of this.

# Tips 

- comment out the return to execute commands w/o a device present:
```python
        try:
            device = list(devices.values()).pop()
        except IndexError:
            self.line("Device not found")
            return
```

- Filter wireshark traffic via dst.port? 
