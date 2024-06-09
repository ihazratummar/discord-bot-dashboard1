from flask import Flask , render_template ,request , jsonify, session, redirect
from  utils import get_token, get_user_guild , get_bot_guilds, get_mutual_guild, get_guild_data


app = Flask(__name__)

app.config['SECRET_KEY'] = "this_is_a_secret"

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/oauth/discord')
def oauth():
    token = get_token(request.args.get("code"))
    session['token'] = token
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'token' not in session:
        return redirect("https://discord.com/oauth2/authorize?client_id=1108627218520887306&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Foauth%2Fdiscord&scope=guilds+identify")
    user_guild = get_user_guild(session.get('token'))
    bot_guild = get_bot_guilds()
    mutual_guilds = get_mutual_guild(user_guild, bot_guild)
    return render_template('dashboard.html', guilds = mutual_guilds)


@app.route('/guild/<guild_id>/main/')
def guild(guild_id: int):
    if 'token' not in session:
        return redirect("https://discord.com/oauth2/authorize?client_id=1108627218520887306&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Foauth%2Fdiscord&scope=guilds+identify")
    guild_info = get_guild_data(guild_id)
    if not guild_info:
        return redirect('/dashboard')
    return render_template('guild.html', guild =guild_info)

@app.route('/guild/<guild_id>/settings/')
def guild_settings(guild_id: int):
    if 'token' not in session:
        return redirect("https://discord.com/oauth2/authorize?client_id=1108627218520887306&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Foauth%2Fdiscord&scope=guilds+identify")
    guild_info = get_guild_data(guild_id)
    if not guild_info:
        return redirect('/dashboard')
    return render_template('settings.html', guild =guild_info)

@app.route('/guild/<guild_id>/announcements/')
def guild_announcements(guild_id: int):
    if 'token' not in session:
        return redirect("https://discord.com/oauth2/authorize?client_id=1108627218520887306&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Foauth%2Fdiscord&scope=guilds+identify")
    guild_info = get_guild_data(guild_id)
    if not guild_info:
        return redirect('/dashboard')
    return render_template('annoucements.html', guild =guild_info)

@app.route('/guild/<guild_id>/commands/')
def guild_commands(guild_id: int):
    if 'token' not in session:
        return redirect("https://discord.com/oauth2/authorize?client_id=1108627218520887306&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Foauth%2Fdiscord&scope=guilds+identify")
    guild_info = get_guild_data(guild_id)
    if not guild_info:
        return redirect('/dashboard')
    return render_template('commands.html', guild =guild_info)

@app.route('/guild/<guild_id>/autoroles/')
def guild_autoroles(guild_id: int):
    if 'token' not in session:
        return redirect("https://discord.com/oauth2/authorize?client_id=1108627218520887306&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Foauth%2Fdiscord&scope=guilds+identify")
    guild_info = get_guild_data(guild_id)
    if not guild_info:
        return redirect('/dashboard')
    return render_template('autoroles.html', guild =guild_info)

@app.route('/guild/<guild_id>/premium/')
def guild_premium(guild_id: int):
    if 'token' not in session:
        return redirect("https://discord.com/oauth2/authorize?client_id=1108627218520887306&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Foauth%2Fdiscord&scope=guilds+identify")
    guild_info = get_guild_data(guild_id)
    if not guild_info:
        return redirect('/dashboard')
    return render_template('premium.html', guild =guild_info)


@app.route('/status')
def status():
    if 'token' not in session:
        return redirect("https://discord.com/oauth2/authorize?client_id=1108627218520887306&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Foauth%2Fdiscord&scope=guilds+identify")
    user_guild = get_user_guild(session.get('token'))
    bot_guild = get_bot_guilds()
    mutual_guilds = get_mutual_guild(user_guild, bot_guild)
    return render_template('status.html', guilds = mutual_guilds)

@app.route('/commands')
def commands():
    return render_template('main-commands.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug= True)