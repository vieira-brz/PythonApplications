from instabot import Bot

# Criando a instância do bot
bot = Bot()

# Credenciais de login
username = ''
password = ''

# Fazendo login
bot.login(username=username, password=password)

# Seguindo um usuário
bot.follow('neymarjr')

# Outras opções possíveis com o bot:

# 1. Deixar de seguir um usuário
bot.unfollow('neymarjr')

# 2. Curtir a última postagem de um usuário
bot.like_user('neymarjr', amount=1)  # 'amount' é o número de postagens a curtir

# 3. Curtir uma lista de hashtags
hashtags = ['football', 'soccer', 'championsleague']
for hashtag in hashtags:
    bot.like_hashtag(hashtag, amount=5)  # Curtir as primeiras 5 postagens de cada hashtag

# 4. Comentar em uma postagem
bot.comment('https://www.instagram.com/p/POST_URL/', 'Amazing post!')

# 5. Seguir uma lista de usuários
users_to_follow = ['user1', 'user2', 'user3']
for user in users_to_follow:
    bot.follow(user)

# 6. Enviar uma mensagem direta (DM)
bot.send_message("Hello from instabot!", ['user1', 'user2'])

# 7. Obter seguidores de um usuário
followers = bot.get_user_followers('neymarjr')
print(followers)

# 8. Obter quem o usuário segue
following = bot.get_user_following('neymarjr')
print(following)

# 9. Deixar de seguir todos os usuários que você segue
bot.unfollow_everyone()

# 10. Baixar imagens de uma hashtag específica
bot.download_photos_by_hashtag('travel', amount=5)

# 11. Enviar foto para o feed
bot.upload_photo("path_to_image.jpg", caption="This is an amazing picture!")

# 12. Curtir postagens de todos os seguidores de um usuário
followers_of_user = bot.get_user_followers('neymarjr')
for follower in followers_of_user:
    bot.like_user(follower, amount=2)  # Curtir as 2 últimas postagens de cada seguidor

# 13. Curtir postagens específicas por URL
bot.like('https://www.instagram.com/p/POST_URL/')

# 14. Deixar de seguir todos os seguidores
bot.unfollow_non_followers()

# 15. Deixar de seguir usuários que não seguem de volta
bot.unfollow_non_followers()

# Logout
bot.logout()