from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название меню')

    def __str__(self):
        return self.name


class ChieldMenu(models.Model):
    chield_name = models.OneToOneField(
        Menu,
        unique=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Меню',
        related_name='chield_name',
    )
    father_name = models.ForeignKey(
        Menu,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Отец',
        related_name='father_name'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['chield_name', 'father_name'], name='unique_parrents'
            ),
            models.CheckConstraint(
                name="self_father",
                check=~models.Q(chield_name=models.F("father_name")),
            ),
        ]
