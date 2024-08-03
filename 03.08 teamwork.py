#How many Pokémons are with 'Type 1' == Water as a % of total?
type1_water = pokemon_df[pokemon_df['Type 1'] == 'Water'].shape[0]

type1_total = pokemon_df['Type 1'].shape[0]

water = (type1_water / type1_total) * 100
print(f'There are {water}% of pokemons with Type 1 = Water')


#What is the maximum 'Speed' value? What is the minimum 'Speed' value? What is the difference between max and min 'Speed'?
max_speed = pokemon_df['Speed'].max()
min_speed = pokemon_df['Speed'].min()
difference_between = max_speed - min_speed

print(f'Difference between max and min speed is {difference_between}')

#Filter the DataFrame to include only the Pokémon with 'Speed' >= 80. 
#How many Pokémon meet this criterion? Display this DataFrame using your preferred visualization method.

speed_more_than_80 = pokemon_df[pokemon_df['Speed']>= 80]
how_many = speed_more_than_80.shape[0]
print(f'{how_many} pokemon meet this criterion.')
plt.hist(speed_more_than_80['Speed'], bins = 4, color = 'pink', edgecolor = 'black')
plt.grid(linestyle = '--')
