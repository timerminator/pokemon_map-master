# Generated by Django 2.2.3 on 2020-11-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0022_remove_pokemonelementtype_strong_against'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonelementtype',
            name='strong_against',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='_pokemonelementtype_strong_against_+', to='pokemon_entities.PokemonElementType'),
        ),
    ]
