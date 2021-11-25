# How to define shell commands
## Creating your first command
1. After you have [installed the *Shell commands* plugin](https://github.com/Taitava/obsidian-shellcommands#installation--usage), open up the settings modal and select *Shell commands* from the left side menu:
	![[Settings-menu.png]]
	
2. You'll see an empty list of shell commands:
	![[Settings-main-no-shell-commands.png]]
	
3. Click on the *New command* button. An empty shell command will appear:
	![[Settings-main-new-shell-command.png]]
	
4. Type a shell command to the *Enter your command* text field. You can use [[Example shell commands|some example shell commands]].
5. Settings are immediately saved when changes are made.

## Main controls for shell commands
![[Settings-main-new-shell-command.png]]
In addition to the actual shell command text field, there are some other controls in the picture above:
- *Command #0* is just a serial number for the shell command. You can replace this text with an [[alias]].
- <svg viewBox="0 0 100 100" class="run-command" width="16" height="16"><path fill="currentColor" stroke="currentColor" d="M37,16c-4.4,0-8.3,3.3-9.2,7.6l-11.6,52c-0.5,2.2,0,4.3,1.2,5.9c1.2,1.6,3.2,2.6,5.4,2.6H79c4.4,0,8.3-3.3,9.2-7.6 l11.6-52c0.5-2.2,0-4.3-1.2-5.9C97.4,17,95.4,16,93.2,16L37,16z M37,20h56.2c1.1,0,1.8,0.4,2.2,1c0.5,0.6,0.7,1.4,0.4,2.6l-1,4.4 H30.8l0.8-3.6C32.1,22.2,34.8,20,37,20z M29.9,32H94l-9.6,43.6C83.9,77.8,81.2,80,79,80H22.8c-1.1,0-1.8-0.4-2.2-1 c-0.5-0.6-0.7-1.4-0.4-2.6L29.9,32z M0,36v4h19.6l0.9-4L0,36z M36.7,38c-0.8,0.1-1.4,0.7-1.6,1.5l-3.5,14c-0.2,0.6,0,1.2,0.4,1.7 c0.4,0.5,1,0.8,1.6,0.8H81c0.9,0,1.7-0.6,1.9-1.5l3.5-14c0.2-0.6,0-1.3-0.4-1.8c-0.4-0.5-1-0.8-1.6-0.8H37.1c-0.1,0-0.1,0-0.2,0 C36.9,38,36.8,38,36.7,38L36.7,38z M38.7,42h43.2l-2.4,10H36.2L38.7,42z M0,52v4h16l0.9-4H0z M0,68v4h12.4l0.9-4H0z"></path></svg> *Execute now*: A quick way to test your command right away.
- <svg viewBox="0 0 100 100" class="gear" width="16" height="16"><path fill="currentColor" stroke="currentColor" d="M44.4,4c-1,0-1.8,0.7-2,1.7l-1.9,11.9c-2.3,0.7-4.6,1.6-6.7,2.7l-9.8-7c-0.8-0.6-1.9-0.5-2.6,0.2l-7.8,7.8 c-0.7,0.7-0.8,1.8-0.2,2.6l6.9,9.9c-1.2,2.1-2.1,4.4-2.8,6.7l-11.9,2c-1,0.2-1.7,1-1.7,2v11c0,1,0.7,1.8,1.6,2l11.9,2.1 c0.7,2.4,1.6,4.6,2.8,6.7l-7,9.8c-0.6,0.8-0.5,1.9,0.2,2.6l7.8,7.8c0.7,0.7,1.8,0.8,2.6,0.2l9.9-6.9c2.1,1.2,4.3,2.1,6.7,2.8 l2,11.9c0.2,1,1,1.7,2,1.7h11c1,0,1.8-0.7,2-1.7l2.1-12c2.3-0.7,4.6-1.6,6.7-2.8l10,7c0.8,0.6,1.9,0.5,2.6-0.2l7.8-7.8 c0.7-0.7,0.8-1.8,0.2-2.6l-7.1-9.9c1.1-2.1,2.1-4.3,2.7-6.6l12-2.1c1-0.2,1.7-1,1.7-2v-11c0-1-0.7-1.8-1.7-2l-12-2 c-0.7-2.3-1.6-4.5-2.7-6.6l7-10c0.6-0.8,0.5-1.9-0.2-2.6l-7.8-7.8c-0.7-0.7-1.8-0.8-2.6-0.2l-9.8,7.1c-2.1-1.2-4.3-2.1-6.7-2.8 l-2.1-12c-0.2-1-1-1.7-2-1.7L44.4,4z M46.1,8h7.6l2,11.4c0.1,0.8,0.7,1.4,1.5,1.6c2.9,0.7,5.7,1.9,8.2,3.4 c0.7,0.4,1.6,0.4,2.2-0.1l9.4-6.7l5.4,5.4l-6.7,9.5c-0.5,0.6-0.5,1.5-0.1,2.2c1.5,2.5,2.6,5.2,3.4,8.1c0.2,0.8,0.8,1.4,1.6,1.5 L92,46.1v7.6l-11.4,2c-0.8,0.1-1.4,0.7-1.6,1.5c-0.7,2.9-1.9,5.6-3.4,8.1c-0.4,0.7-0.4,1.6,0.1,2.2l6.8,9.4l-5.4,5.4l-9.5-6.7 c-0.7-0.5-1.5-0.5-2.2-0.1c-2.5,1.5-5.2,2.7-8.2,3.4c-0.8,0.2-1.3,0.8-1.5,1.6l-2,11.4h-7.6l-1.9-11.3c-0.1-0.8-0.7-1.4-1.5-1.6 c-2.9-0.7-5.7-1.9-8.2-3.4c-0.7-0.4-1.5-0.4-2.2,0.1l-9.4,6.6l-5.4-5.4l6.6-9.3c0.5-0.7,0.5-1.5,0.1-2.2c-1.5-2.5-2.7-5.3-3.4-8.2 c-0.2-0.8-0.8-1.3-1.6-1.5L8,53.7v-7.6l11.3-1.9c0.8-0.1,1.4-0.7,1.6-1.5c0.7-2.9,1.9-5.7,3.4-8.2c0.4-0.7,0.4-1.5-0.1-2.2 l-6.6-9.4l5.4-5.4l9.3,6.7c0.6,0.5,1.5,0.5,2.2,0.1c2.5-1.5,5.3-2.7,8.2-3.4c0.8-0.2,1.4-0.8,1.5-1.6L46.1,8z M50,34 c-8.8,0-16,7.2-16,16s7.2,16,16,16s16-7.2,16-16S58.8,34,50,34z M50,38c6.7,0,12,5.3,12,12s-5.3,12-12,12s-12-5.3-12-12 S43.3,38,50,38z"></path></svg> *Alias, Confirmation*: Allows you to define an [[alias]] for the shell command; and enable a confirmation question to be asked every time before execution.
- <svg viewBox="0 0 100 100" class="lines-of-text" width="16" height="16"><path fill="currentColor" stroke="currentColor" d="M16,10c-3.3,0-6,2.7-6,6v68c0,3.3,2.7,6,6,6h68c3.3,0,6-2.7,6-6V16c0-3.3-2.7-6-6-6L16,10z M16,14h68c1.1,0,2,0.9,2,2v68 c0,1.1-0.9,2-2,2H16c-1.1,0-2-0.9-2-2V16C14,14.9,14.9,14,16,14z M22,24v4h52v-4H22z M22,36v4h34v-4L22,36z M22,48v4h52v-4H22z M22,60v4h34v-4H22z M22,72v4h52v-4H22z"></path></svg> *Stdout/stderr handling, Ignore errors*: Allows you to define [[Output channels|how the shell command's output should be processed]]; and possible [[Ignoring errors|ignoring of errors]].
- <svg viewBox="0 0 100 100" class="stacked-levels" width="16" height="16"><path fill="currentColor" stroke="currentColor" d="M12,4c-1.1,0-2,0.9-2,2v20c0,1.1,0.9,2,2,2h14v21.7c0,0.2,0,0.4,0,0.7V84c0,1.1,0.9,2,2,2h26v8c0,1.1,0.9,2,2,2h32 c1.1,0,2-0.9,2-2V74c0-1.1-0.9-2-2-2H56c-1.1,0-2,0.9-2,2v8H30V52h24v8c0,1.1,0.9,2,2,2h32c1.1,0,2-0.9,2-2V40c0-1.1-0.9-2-2-2 H56c-1.1,0-2,0.9-2,2v8H30V28h14c1.1,0,2-0.9,2-2V6c0-1.1-0.9-2-2-2L12,4z M14,8h28v16H28.3c-0.1,0-0.2,0-0.3,0 c-0.1,0-0.2,0-0.3,0H14L14,8z M58,42h28v16H58v-7.7c0-0.2,0-0.4,0-0.7V42z M58,76h28v16H58v-7.7c0-0.2,0-0.4,0-0.7V76z"></path></svg> *Shell selection, Operating system specific shell commands*: Advanced features for choosing a [[Shells|shell]] where the shell command will be executed in; and defining different versions of the shell command for different operating systems, in case you synchronize your vault between multiple OSes.
- <svg viewBox="0 0 100 100" class="trash" width="16" height="16"><path fill="currentColor" stroke="currentColor" stroke-width="2" d="M42,4c-3.3,0-6,2.7-6,6v4H20.3c-0.1,0-0.2,0-0.3,0c-0.1,0-0.2,0-0.3,0H16c-0.7,0-1.4,0.4-1.8,1c-0.4,0.6-0.4,1.4,0,2 c0.4,0.6,1,1,1.8,1h2v72c0,3.3,2.7,6,6,6h52c3.3,0,6-2.7,6-6V18h2c0.7,0,1.4-0.4,1.8-1c0.4-0.6,0.4-1.4,0-2c-0.4-0.6-1-1-1.8-1 h-3.7c-0.2,0-0.4,0-0.7,0H64v-4c0-3.3-2.7-6-6-6L42,4z M42,8h16c1.1,0,2,0.9,2,2v4H40v-4C40,8.9,40.9,8,42,8z M22,18h15.7 c0.2,0,0.4,0,0.7,0h23.3c0.2,0,0.4,0,0.7,0H78v72c0,1.1-0.9,2-2,2H24c-1.1,0-2-0.9-2-2V18z M38,28c-1.1,0-2,0.9-2,2v50 c0,0.7,0.4,1.4,1,1.8s1.4,0.4,2,0s1-1,1-1.8V30c0-0.5-0.2-1.1-0.6-1.4C39,28.2,38.5,28,38,28z M50,28c-1.1,0-2,0.9-2,2v50 c0,0.7,0.4,1.4,1,1.8c0.6,0.4,1.4,0.4,2,0s1-1,1-1.8V30c0-0.5-0.2-1.1-0.6-1.4C51,28.2,50.5,28,50,28z M62,28c-1.1,0-2,0.9-2,2v50 c0,0.7,0.4,1.4,1,1.8c0.6,0.4,1.4,0.4,2,0s1-1,1-1.8V30c0-0.5-0.2-1.1-0.6-1.4C63,28.2,62.5,28,62,28z"></path></svg> *Delete this shell command*. Will ask a confirmation. Deletion cannot be undone, unless you have [[Backups|backups of the plugin's settings]].