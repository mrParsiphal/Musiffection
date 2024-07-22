from rest_framework import serializers
import mutagen

from .models import MusicModel, AuditionModel


class MusicSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if not validated_data.get('img'):
            validated_data['img'] = None
        if not validated_data.get('author'):
            validated_data['author'] = 'неизвестен'
        if not validated_data.get('text'):
            validated_data['text'] = None
        validated_data['auditions'] = 0
        validated_data['rating'] = 0
        mutagen_data = mutagen.File('../musics files/musics/' + validated_data['file'])
        sec_dur = mutagen_data.info.length
        validated_data['duration'] = (f'{int(sec_dur // 60)}'.rjust(2, '0') +
                                      ':' + f'{int(sec_dur % 60)}'.rjust(2, '0'))
        return MusicModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.img = validated_data.get('img', instance.img)
        instance.author = validated_data.get('author', instance.author)
        instance.text = validated_data.get('text', instance.text)
        instance.auditions = validated_data.get('auditions', instance.auditions)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.tegs.set(validated_data.get('tegs', instance.tegs))
        instance.genres.set(validated_data.get('genres', instance.genres))
        instance.save()
        return instance

    class Meta:
        model = MusicModel
        fields = '__all__'


class AuditionSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if not validated_data.get('attitude'):
            validated_data['attiiude'] = None
        return AuditionModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.attitude = validated_data.get('attitude', instance.attitude)

        instance.save()
        return instance

    class Meta:
        model = AuditionModel
        fields = '__all__'