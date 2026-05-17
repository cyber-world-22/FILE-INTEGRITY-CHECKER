# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SAGAR SHAMRAO MAKUDE

*INTERN ID*: CTIS8277

*DOMAIN*: ETHICAL HACKING AND CYBERSECURITY

*DURATION*: 16 WEEKS

*MENTOR*: NEELA SANTOSH

##The File Integrity Checker is a cybersecurity-based Python project developed to monitor and verify the integrity of files by using cryptographic hash functions. The main purpose of this project is to detect unauthorized modifications, corruption, or tampering of files by generating and comparing unique hash values. This project demonstrates the practical implementation of file integrity monitoring concepts that are widely used in ethical hacking, cybersecurity, digital forensics, and system security.

In modern computer systems, protecting the integrity of important files is a critical aspect of cybersecurity. Files can be modified intentionally by attackers, malware, ransomware, or unauthorized users, and they can also become corrupted accidentally. To address this issue, the File Integrity Checker continuously verifies whether a file remains unchanged from its original state. The project uses the SHA-256 hashing algorithm from Python’s built-in hashlib library to generate a unique digital fingerprint for each file.

The working principle of this project is based on cryptographic hashing. A hash function converts file data into a fixed-length hash value. Even a very small modification in the file, such as changing a single character, produces a completely different hash value due to the avalanche effect of cryptographic algorithms. This property makes hashing highly effective for integrity verification. The project first generates the original hash value of a selected file and stores it temporarily. Later, when the file is checked again, a new hash value is generated and compared with the original one. If both hash values match, the file integrity is maintained. If the hash values differ, the project identifies that the file has been modified or tampered with.

The project is developed using the Python programming language because of its simplicity, readability, and powerful built-in libraries. The hashlib library is used for implementing SHA-256 hashing, while the os module is used to verify file existence and handle file-related operations. The file is read in binary mode (rb) to ensure accurate processing of all file types, including text files, images, PDFs, executable files, and multimedia content. To improve performance and memory efficiency, files are processed in chunks instead of loading the entire file into memory at once.
