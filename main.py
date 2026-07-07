import os
import sys
import threading
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import platform
from kivy.metrics import dp
import yt_dlp

# تنظیمات پنجره
Window.size = (620, 720)
Window.clearcolor = (0, 0, 0, 1)

class DownloaderUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(8)
        self.padding = dp(15)
        
        # متغیرها
        self.download_thread = None
        self.is_downloading = False
        
        # تنظیمات فونت پیش‌فرض
        self.font_name = 'Roboto'
        
        self.build_ui()
    
    def build_ui(self):
        # ========== لوگو ==========
        logo_layout = BoxLayout(size_hint_y=None, height=dp(60))
        logo_layout.size_hint_x = 1
        logo_layout.spacing = dp(10)
        
        # تلاش برای بارگذاری لوگو
        logo_paths = ['./Brothers.png', './brothers.png', './logo.png']
        logo_found = False
        
        for path in logo_paths:
            if os.path.exists(path):
                try:
                    logo_img = Image(source=path, size_hint=(None, None), size=(dp(50), dp(50)))
                    logo_img.pos_hint = {'center_x': 0.5}
                    logo_layout.add_widget(logo_img)
                    logo_found = True
                    break
                except:
                    continue
        
        if not logo_found:
            logo_label = Label(
                text='B',
                font_size=dp(40),
                color=(0.2, 0.6, 0.86, 1),
                bold=True,
                size_hint=(None, None),
                size=(dp(50), dp(50)),
                pos_hint={'center_x': 0.5}
            )
            logo_layout.add_widget(logo_label)
        
        self.add_widget(logo_layout)
        
        # ========== URL Input ==========
        url_box = BoxLayout(size_hint_y=None, height=dp(80))
        url_box.spacing = dp(6)
        
        self.url_input = TextInput(
            hint_text='Paste your link here...',
            multiline=False,
            size_hint_x=0.8,
            font_size=dp(13),
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0.2, 0.6, 0.86, 1),
            padding=[dp(12), dp(10), dp(12), dp(10)]
        )
        
        self.paste_btn = Button(
            text='Paste',
            size_hint_x=0.2,
            font_size=dp(13),
            background_color=(0.2, 0.6, 0.86, 1),
            color=(1, 1, 1, 1)
        )
        self.paste_btn.bind(on_press=self.paste_from_clipboard)
        
        url_box.add_widget(self.url_input)
        url_box.add_widget(self.paste_btn)
        self.add_widget(url_box)
        
        # ========== Download Type ==========
        type_box = GridLayout(
            cols=3,
            size_hint_y=None,
            height=dp(50),
            spacing=dp(10),
            padding=[dp(10), dp(5), dp(10), dp(5)]
        )
        
        self.video_check = CheckBox(active=False)
        self.video_check.bind(active=self.update_download_options)
        video_label = Label(text='Video Only', color=(1, 1, 1, 1))
        video_box = BoxLayout(orientation='horizontal')
        video_box.add_widget(self.video_check)
        video_box.add_widget(video_label)
        
        self.audio_check = CheckBox(active=False)
        self.audio_check.bind(active=self.update_download_options)
        audio_label = Label(text='Audio Only', color=(1, 1, 1, 1))
        audio_box = BoxLayout(orientation='horizontal')
        audio_box.add_widget(self.audio_check)
        audio_box.add_widget(audio_label)
        
        self.both_check = CheckBox(active=True)
        self.both_check.bind(active=self.update_download_options)
        both_label = Label(text='Video + Audio', color=(1, 1, 1, 1))
        both_box = BoxLayout(orientation='horizontal')
        both_box.add_widget(self.both_check)
        both_box.add_widget(both_label)
        
        type_box.add_widget(video_box)
        type_box.add_widget(audio_box)
        type_box.add_widget(both_box)
        self.add_widget(type_box)
        
        # ========== Download Settings ==========
        settings_box = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=dp(180),
            spacing=dp(6),
            padding=[dp(10), dp(8), dp(10), dp(8)]
        )
        
        # Quality
        quality_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
        quality_label = Label(text='Quality:', size_hint_x=0.3, color=(1, 1, 1, 1), halign='right')
        quality_label.bind(size=quality_label.setter('text_size'))
        
        self.quality_spinner = Spinner(
            text='Best Available',
            values=['Best Available', '2160p (4K)', '1440p (2K)', '1080p (Full HD)', 
                   '720p (HD)', '480p (SD)', '360p', '240p'],
            size_hint_x=0.7,
            font_size=dp(13),
            background_color=(0.1, 0.1, 0.1, 1),
            color=(1, 1, 1, 1)
        )
        quality_row.add_widget(quality_label)
        quality_row.add_widget(self.quality_spinner)
        settings_box.add_widget(quality_row)
        
        # Audio Format
        audio_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
        audio_label = Label(text='Audio Format:', size_hint_x=0.3, color=(1, 1, 1, 1), halign='right')
        audio_label.bind(size=audio_label.setter('text_size'))
        
        self.audio_spinner = Spinner(
            text='MP3',
            values=['MP3', 'M4A', 'FLAC', 'WAV', 'OPUS'],
            size_hint_x=0.7,
            font_size=dp(13),
            background_color=(0.1, 0.1, 0.1, 1),
            color=(1, 1, 1, 1)
        )
        audio_row.add_widget(audio_label)
        audio_row.add_widget(self.audio_spinner)
        settings_box.add_widget(audio_row)
        
        # Video Format
        video_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
        video_format_label = Label(text='Video Format:', size_hint_x=0.3, color=(1, 1, 1, 1), halign='right')
        video_format_label.bind(size=video_format_label.setter('text_size'))
        
        self.video_spinner = Spinner(
            text='MP4',
            values=['MP4', 'MKV', 'WEBM'],
            size_hint_x=0.7,
            font_size=dp(13),
            background_color=(0.1, 0.1, 0.1, 1),
            color=(1, 1, 1, 1)
        )
        video_row.add_widget(video_format_label)
        video_row.add_widget(self.video_spinner)
        settings_box.add_widget(video_row)
        
        self.add_widget(settings_box)
        
        # ========== Save Location ==========
        save_box = BoxLayout(size_hint_y=None, height=dp(70), spacing=dp(6))
        
        self.save_path = TextInput(
            text=os.path.join(os.path.expanduser('~'), 'Downloads'),
            multiline=False,
            size_hint_x=0.7,
            font_size=dp(13),
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            padding=[dp(12), dp(10), dp(12), dp(10)]
        )
        
        self.browse_btn = Button(
            text='Browse',
            size_hint_x=0.3,
            font_size=dp(13),
            background_color=(0.2, 0.6, 0.86, 1),
            color=(1, 1, 1, 1)
        )
        self.browse_btn.bind(on_press=self.browse_folder)
        
        save_box.add_widget(self.save_path)
        save_box.add_widget(self.browse_btn)
        self.add_widget(save_box)
        
        # ========== Progress Bar ==========
        self.progress_bar = ProgressBar(
            max=100,
            value=0,
            size_hint_y=None,
            height=dp(36)
        )
        self.add_widget(self.progress_bar)
        
        # ========== Download Button ==========
        self.download_btn = Button(
            text='DOWNLOAD',
            size_hint_y=None,
            height=dp(44),
            font_size=dp(15),
            bold=True,
            background_color=(0.2, 0.6, 0.86, 1),
            color=(1, 1, 1, 1)
        )
        self.download_btn.bind(on_press=self.start_download)
        self.add_widget(self.download_btn)
        
        # ========== Status ==========
        self.status_label = Label(
            text='Ready to download',
            color=(0.2, 0.6, 0.86, 1),
            font_size=dp(13),
            bold=True,
            size_hint_y=None,
            height=dp(30)
        )
        self.add_widget(self.status_label)
        
        # ========== Info ==========
        self.info_label = Label(
            text='',
            color=(0.4, 0.4, 0.4, 1),
            font_size=dp(11),
            size_hint_y=None,
            height=dp(22)
        )
        self.add_widget(self.info_label)
        
        self.update_download_options(None, None)
    
    def update_download_options(self, instance, value):
        """به‌روزرسانی گزینه‌های دانلود"""
        try:
            # اطمینان از اینکه حداقل یک گزینه انتخاب شده
            if not self.video_check.active and not self.audio_check.active and not self.both_check.active:
                self.both_check.active = True
            
            # غیرفعال کردن کیفیت و فرمت ویدیو در حالت صوتی
            if self.audio_check.active and not self.video_check.active and not self.both_check.active:
                self.quality_spinner.disabled = True
                self.video_spinner.disabled = True
            else:
                self.quality_spinner.disabled = False
                self.video_spinner.disabled = False
        except Exception as e:
            print(f'Error in update_download_options: {e}')
    
    def paste_from_clipboard(self, instance):
        """چسباندن از کلیپ‌بورد"""
        try:
            from kivy.core.clipboard import Clipboard
            text = Clipboard.paste()
            if text:
                self.url_input.text = text
                self.update_status('Link pasted successfully!', (0.18, 0.8, 0.44, 1))
                Clock.schedule_once(lambda dt: self.update_status('Ready to download', (0.2, 0.6, 0.86, 1)), 2)
        except Exception as e:
            print(f'Error in paste_from_clipboard: {e}')
    
    def update_status(self, text, color=None):
        """به‌روزرسانی وضعیت"""
        try:
            self.status_label.text = text
            if color:
                self.status_label.color = color
        except Exception as e:
            print(f'Error in update_status: {e}')
    
    def browse_folder(self, instance):
        """انتخاب پوشه ذخیره‌سازی"""
        try:
            content = BoxLayout(orientation='vertical')
            filechooser = FileChooserListView(
                path=os.path.expanduser('~'),
                dirselect=True
            )
            content.add_widget(filechooser)
            
            btn_box = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
            cancel_btn = Button(text='Cancel')
            select_btn = Button(text='Select')
            btn_box.add_widget(cancel_btn)
            btn_box.add_widget(select_btn)
            content.add_widget(btn_box)
            
            popup = Popup(
                title='Select Download Folder',
                content=content,
                size_hint=(0.9, 0.9)
            )
            
            def select_folder(instance):
                if filechooser.selection:
                    self.save_path.text = filechooser.selection[0]
                popup.dismiss()
            
            cancel_btn.bind(on_press=popup.dismiss)
            select_btn.bind(on_press=select_folder)
            
            popup.open()
        except Exception as e:
            print(f'Error in browse_folder: {e}')
    
    def show_error(self, title, message):
        """نمایش خطا"""
        try:
            content = BoxLayout(orientation='vertical', padding=dp(10))
            content.add_widget(Label(text=message, color=(1, 1, 1, 1)))
            
            btn = Button(text='OK', size_hint_y=None, height=dp(50))
            content.add_widget(btn)
            
            popup = Popup(
                title=title,
                content=content,
                size_hint=(0.8, 0.4)
            )
            btn.bind(on_press=popup.dismiss)
            popup.open()
        except Exception as e:
            print(f'Error in show_error: {e}')
    
    def get_quality_format(self, quality_text):
        """دریافت فرمت کیفیت"""
        try:
            quality_map = {
                'Best Available': 'bestvideo+bestaudio/best',
                '2160p (4K)': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
                '1440p (2K)': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',
                '1080p (Full HD)': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
                '720p (HD)': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
                '480p (SD)': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
                '360p': 'bestvideo[height<=360]+bestaudio/best[height<=360]',
                '240p': 'bestvideo[height<=240]+bestaudio/best[height<=240]'
            }
            return quality_map.get(quality_text, 'bestvideo+bestaudio/best')
        except Exception as e:
            print(f'Error in get_quality_format: {e}')
            return 'bestvideo+bestaudio/best'
    
    def get_audio_format(self, audio_text):
        """دریافت فرمت صوتی"""
        try:
            audio_map = {
                'MP3': 'mp3',
                'M4A': 'm4a',
                'FLAC': 'flac',
                'WAV': 'wav',
                'OPUS': 'opus'
            }
            return audio_map.get(audio_text, 'mp3')
        except Exception as e:
            print(f'Error in get_audio_format: {e}')
            return 'mp3'
    
    def get_video_format(self, video_text):
        """دریافت فرمت ویدیو"""
        try:
            video_map = {
                'MP4': 'mp4',
                'MKV': 'mkv',
                'WEBM': 'webm'
            }
            return video_map.get(video_text, 'mp4')
        except Exception as e:
            print(f'Error in get_video_format: {e}')
            return 'mp4'
    
    def start_download(self, instance):
        """شروع دانلود"""
        try:
            if self.is_downloading:
                return
            
            url = self.url_input.text.strip()
            if not url:
                self.show_error('Error', 'Please enter a URL')
                return
            
            if not self.save_path.text:
                self.show_error('Error', 'Please select a save location')
                return
            
            self.is_downloading = True
            self.download_btn.text = 'DOWNLOADING...'
            self.download_btn.disabled = True
            self.update_status('Starting download...', (0.96, 0.62, 0.07, 1))
            self.progress_bar.value = 0
            self.info_label.text = ''
            
            # شروع دانلود در یک ترد جداگانه
            self.download_thread = threading.Thread(target=self.download_media, args=(url,))
            self.download_thread.daemon = True
            self.download_thread.start()
        except Exception as e:
            print(f'Error in start_download: {e}')
            self.show_error('Error', f'An error occurred: {str(e)}')
            self.reset_ui()
    
    def reset_ui(self):
        """بازنشانی UI"""
        try:
            self.is_downloading = False
            self.download_btn.text = 'DOWNLOAD'
            self.download_btn.disabled = False
            self.progress_bar.value = 0
        except Exception as e:
            print(f'Error in reset_ui: {e}')
    
    def download_media(self, url):
        """عملیات دانلود"""
        try:
            download_video = self.video_check.active
            download_audio = self.audio_check.active
            download_both = self.both_check.active
            
            quality = self.quality_spinner.text
            audio_format = self.get_audio_format(self.audio_spinner.text)
            video_format = self.get_video_format(self.video_spinner.text)
            save_path = self.save_path.text
            
            # پیدا کردن ffmpeg
            ffmpeg_path = './ffmpeg.exe' if platform == 'win' else '/usr/bin/ffmpeg'
            if not os.path.exists(ffmpeg_path):
                ffmpeg_path = 'ffmpeg'  # fallback to system PATH
            
            ydl_opts = {
                'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
                'merge_output_format': video_format,
                'ffmpeg_location': ffmpeg_path,
                'progress_hooks': [self.ydl_progress_hook],
                'verbose': False,
                'no_warnings': True,
                'extract_flat': False,
                'ignoreerrors': True,
                'no_color': True,
                'geo_bypass': True,
                'socket_timeout': 30,
                'retries': 10,
                'fragment_retries': 10,
                'skip_unavailable_fragments': True,
                'keepvideo': False,
            }
            
            if download_audio and not download_video and not download_both:
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': audio_format,
                    'preferredquality': '320',
                }]
            elif download_video and not download_audio and not download_both:
                ydl_opts['format'] = self.get_quality_format(quality)
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': video_format,
                }]
            else:
                ydl_opts['format'] = self.get_quality_format(quality)
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': video_format,
                }]
            
            # دریافت اطلاعات ویدیو
            try:
                with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                    info = ydl.extract_info(url, download=False)
                    if info:
                        title = info.get('title', 'Unknown')
                        duration = info.get('duration', 0)
                        duration_str = f'{duration//60}:{duration%60:02d}' if duration else 'Unknown'
                        Clock.schedule_once(lambda dt: setattr(self.info_label, 'text', f'{title} | {duration_str}'))
            except Exception as e:
                print(f'Error getting info: {e}')
            
            # دانلود
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            Clock.schedule_once(lambda dt: self.download_complete())
            
        except Exception as e:
            error_msg = str(e)
            if 'ffmpeg' in error_msg.lower():
                error_msg = 'FFmpeg not found! Please install ffmpeg or place ffmpeg.exe in the program folder.'
            
            Clock.schedule_once(lambda dt: self.download_error(error_msg))
    
    def ydl_progress_hook(self, d):
        """Hook پیشرفت دانلود"""
        try:
            if d['status'] == 'downloading':
                total = d.get('total_bytes') or d.get('total_bytes_estimate', 1)
                downloaded = d.get('downloaded_bytes', 0)
                percentage = int((downloaded / total) * 100) if total > 0 else 0
                
                if percentage > 99:
                    percentage = 99
                
                Clock.schedule_once(lambda dt, p=percentage: setattr(self.progress_bar, 'value', p))
                
                speed = d.get('speed', 0)
                if speed:
                    speed_mb = speed / 1024 / 1024
                    if speed_mb > 1:
                        speed_text = f'{speed_mb:.2f} MB/s'
                    else:
                        speed_text = f'{speed/1024:.2f} KB/s'
                else:
                    speed_text = 'Calculating...'
                
                eta = d.get('eta', 0)
                if eta:
                    if eta > 3600:
                        eta_text = f'{eta//3600}h {(eta%3600)//60}m'
                    elif eta > 60:
                        eta_text = f'{eta//60}m {eta%60}s'
                    else:
                        eta_text = f'{eta}s'
                else:
                    eta_text = 'Unknown'
                
                Clock.schedule_once(lambda dt: self.update_status(
                    f'Downloading... {speed_text} | ETA: {eta_text}',
                    (0.96, 0.62, 0.07, 1)
                ))
                
            elif d['status'] == 'finished':
                Clock.schedule_once(lambda dt: self.update_status('Processing...', (0.96, 0.62, 0.07, 1)))
                Clock.schedule_once(lambda dt: setattr(self.progress_bar, 'value', 99))
                
            elif d['status'] == 'error':
                Clock.schedule_once(lambda dt: self.update_status('Download error occurred', (0.92, 0.3, 0.24, 1)))
                
        except Exception as e:
            print(f'Error in ydl_progress_hook: {e}')
    
    def download_complete(self):
        """تکمیل دانلود"""
        try:
            self.progress_bar.value = 100
            self.update_status('100% Complete!', (0.18, 0.8, 0.44, 1))
            self.reset_ui()
            
            self.show_error('Success', 'Download completed successfully!')
        except Exception as e:
            print(f'Error in download_complete: {e}')
    
    def download_error(self, error_msg):
        """خطا در دانلود"""
        try:
            self.update_status(f'Error: {error_msg[:40]}...', (0.92, 0.3, 0.24, 1))
            self.reset_ui()
            self.show_error('Download Error', error_msg)
        except Exception as e:
            print(f'Error in download_error: {e}')
            self.reset_ui()

class DownloaderApp(App):
    def build(self):
        self.title = 'Brothers 4.0'
        self.icon = 'Brothers.ico' if os.path.exists('Brothers.ico') else 'brothers.ico'
        return DownloaderUI()

if __name__ == '__main__':
    DownloaderApp().run()