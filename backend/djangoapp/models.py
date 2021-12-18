import datetime
import pytz
from dateutil.relativedelta import relativedelta

from django.db import models
from djangoapp.model_utils import BaseModel


# Create your models here.
class Words(BaseModel):
    word = models.CharField(max_length=255)
    definition = models.TextField()
    bin_number = models.IntegerField(default=0, choices=[(i,i) for i in range(12)])
    available_time = models.DateTimeField(null=True, blank=True)
    incorrect_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.word

    class Meta:
        db_table = "words"
        verbose_name_plural = "words"
        ordering = ['-id']

    BIN_INTERVALS = [
        0,
        relativedelta(seconds=5),
        relativedelta(seconds=25),
        relativedelta(minutes=2),
        relativedelta(minutes=10),
        relativedelta(hours=1),
        relativedelta(hours=5),
        relativedelta(days=1),
        relativedelta(days=5),
        relativedelta(days=25),
        relativedelta(months=4),
    ]

    def get_next_word(self):
        # Base filter for bin and incorrect values.
        base_word = Words.objects.filter(bin_number__range=(0,10), incorrect_counter__lt=10)
        now = datetime.datetime.now(pytz.utc)

        # Check for words already shown up and to be reviewed.
        review_words = base_word.exclude(bin_number=0).filter(
            available_time__isnull=False, available_time__lte=now
        )
        if review_words.count():
            # sort and return higher bin number
            review_word = review_words.order_by('-bin_number')[:1]
        else:
            # Check for new word
            review_word = base_word.filter(bin_number=0)[:1]

        if review_word.count():
            # Return data to be reveiwed.
            return list(review_word.values('id', 'word', 'definition'))[0]
        else:
            error = "you have no more words to review; you are permanently done!"
        possible_future_words = Words.objects.filter(
            bin_number__range=(1,10),
            available_time__isnull=False,
            available_time__gte=now
        )
        if possible_future_words.count() > 0:
            error = "You are temporarily done; please come back later to review more words."
        return {"error": error}

    def mark_as_correct(self):
        # Bin_number += 1, if bin number between 0 and 10.
        # Update available time based on bin
        now = datetime.datetime.now(pytz.utc)
        if self.bin_number >= 0 and self.bin_number < 11:
            self.bin_number += 1
            self.available_time = now + self.BIN_INTERVALS[self.bin_number]
            self.save()

    def mark_as_wrong(self):
        # Mark bin as 1.
        # Update available time based on bin 1.
        # incorrect_counter += 1.
        now = datetime.datetime.now(pytz.utc)
        self.bin_number = 1
        self.available_time = now + self.BIN_INTERVALS[self.bin_number]
        self.incorrect_counter += 1
        self.save()
