# 🍌 BANAN Packages Repo – MonkeyOS Edition 🐒

Welcome to the official **Banan packages repository** for **MonkeyOS**!  

This is where all your `.banapkg` files live, ready to be installed using the **Banan package manager**.

---

## What is BANAN?

**BANAN** is the MonkeyOS package manager.  

It fetches, installs, and resolves dependencies for `.banapkg` files. 

Think of it as **apt-get**, but **monkey chaos style**.  

- Fast installs 🍌  
- Dependency handling 🐒  
- Debug prints for awesome brain

---

## Installing Packages

Use your MonkeyOS Banan client:

```bash
banan install <package-name>
```
Example:
```bash
banan install free-ram
```
### Will automatically:

- Fetch example.banapkg from this repo
- Install dependencies (if any)
- Write the code to the package's install path (usually ~/.bananpkgs)
- Show monkey-approved debug messages

### Package Format (.banapkg)

Each package is a JSON file with the following structure:
```json
{
  "ver": "1.0.0",
  "name": "example-jungles",
  "type": "py",
  "dependent": ["example", "dependencytest"],
  "installplace": "~/.bananpkgs",
  "code": "# Your code goes here\nprint('Hello from example jungles!')"
}
```

### Fields explained:

- ver → package version
- name → package name (used for filename when installed)
- type → file extension (py, txt, etc.)
- dependent → list of other packages required
- installplace → install location
- code → the actual code/content

### Contributing

Want to add a new package? Just:

1. Fork this repo 🍌
  
2. Add a .banapkg file following the template
   
3. Make sure dependencies exist in this repo (or create them!)
   
4. Submit a PR and let the crazed monkeys review 🐒

### Monkey Tips

Ctrl+C → Abort any install (Monkey-approved 🐒💨)

You can use `time banan install <package>` to see how fast BANAN really is when downloading 🚀

### License

MIT License – keep the chaos, credit the original monkeys, no warranty 😎
