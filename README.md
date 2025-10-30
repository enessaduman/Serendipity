## 📚​ Study Orginizer <br>

📘 Overview<br>

Study Organizer is a command-line tool that helps users manage their study goals efficiently.
It allows users to define study plans, log their daily study sessions, and track their overall progress through simple terminal commands.

<h2>How to Run</h2>

  <section id="how-to-run">
  <h2>How to Run</h2>

  <h3>1️⃣ Register & Login</h3>

  <p>
    Before adding study goals or sessions, you need to register a user and log in.  
    The following commands should be run in your terminal.
  </p>

  <div class="cmd-group">
    <h4>Register a new user</h4>
    <pre><code class="bash">$ python register.py --username YourName</code></pre>
  </div>

  <div class="cmd-group">
    <h4>Log in as an existing user</h4>
    <pre><code class="bash">$ python login.py</code></pre>
  </div>

  <p class="note">
    <strong>Note:</strong> The <code>$</code> symbol indicates a terminal command.  
    Do <em>not</em> include it when typing the command yourself.
  </p>

  <hr>

  <p>
    After logging in successfully, your user information will be stored automatically  
    for future sessions and goal tracking.
  </p>

  <style>
    /* Minimal styling for README HTML */
    #how-to-run {
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      line-height: 1.5;
    }
    pre {
      background: #0f1722;
      color: #e6eef8;
      padding: 12px;
      border-radius: 6px;
      overflow: auto;
    }
    code.bash {
      font-family: "SFMono-Regular", Menlo, Monaco, "Roboto Mono", "Courier New", monospace;
    }
    .note {
      background: #fff9e6;
      padding: 8px;
      border-left: 4px solid #ffd24d;
      border-radius: 4px;
    }
    hr {
      border: none;
      border-top: 1px solid #eee;
      margin: 18px 0;
    }
  </style>
</section>
